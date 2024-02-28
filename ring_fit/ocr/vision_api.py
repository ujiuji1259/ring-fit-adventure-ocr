import re
from datetime import date

from google.cloud import vision

from ring_fit.ocr.base import FitResultOcr
from ring_fit.fit_skill import get_fit_skill_from_name
from ring_fit.fit_result import FitResult
from ring_fit.image_downloader import FitResultImage


from dataclasses import dataclass
from typing import Optional
from ring_fit.fit_skill import is_fit_skill, get_fit_skill_from_name
from ring_fit.fit_result import FitResult
import re



def get_reps_from_text(text: str) -> Optional[int]:
    match_obj = re.search('^(\d+)回.*', text)
    if match_obj is None:
        return None

    return int(match_obj.groups()[0])


@dataclass
class VisionApiBox:
    name: str
    left_top_x: int
    left_top_y: int
    right_top_x: int

    def is_left(self):
        return self.left_top_x < 600

    def is_the_same_box(self, left_box: 'VisionApiBox', x_margin: int = 5, y_margin: int = 5) -> bool:
        return (abs(self.left_top_x - left_box.right_top_x) < x_margin
                and abs(self.left_top_y - left_box.left_top_y) < y_margin)
    
    def is_fit_skill_name_box(self) -> bool:
        return is_fit_skill(self.name)
    
    def is_reps_box(self) -> bool:
        reps = get_reps_from_text(self.name)
        return reps is not None

    def is_same_fit_result(self, target_box: 'VisionApiBox', x_half_line: int = 600, y_margin: int = 5) -> bool:
        if abs(self.left_top_y - target_box.left_top_y) > y_margin:
            return False
        
        if self.left_top_x < x_half_line:
            return target_box.left_top_x < x_half_line
        
        return target_box.left_top_x >= x_half_line
    

def list_all_box(response) -> list[VisionApiBox]:
    def _extract_box_info(word):
        text = ''.join([
            symbol.text for symbol in word.symbols
        ])
        left_top_vertice = word.bounding_box.vertices[0]
        right_top_vertice = word.bounding_box.vertices[1]
        return VisionApiBox(text, left_top_vertice.x, left_top_vertice.y, right_top_vertice.x)

    return [
        _extract_box_info(word)
        for page in response.full_text_annotation.pages
        for block in page.blocks
        for paragraph in block.paragraphs
        for word in paragraph.words
    ]

def merge_same_box(boxes: list[VisionApiBox]) -> list[VisionApiBox]:
    result: list[VisionApiBox] = []
    for box in boxes:
        if len(result) > 0 and box.is_the_same_box(result[-1]):
            merged_box = VisionApiBox(
                result[-1].name + box.name,
                box.left_top_x,
                box.left_top_y,
                box.right_top_x
            )
            result = result[:-1] + [merged_box]
        else:
            result.append(box)
    return result


def get_fit_result(boxes: list[VisionApiBox]) -> FitResult:
    results = []
    for i in range(len(boxes)):
        fit_skill_box = boxes[i]
        if not fit_skill_box.is_fit_skill_name_box():
            continue

        reps_candidate = []
        for j in range(i + 1, len(boxes)):
            reps_box = boxes[j]
            if reps_box.is_reps_box() and fit_skill_box.is_same_fit_result(reps_box):
                reps_candidate.append(reps_box)

        if len(reps_candidate) == 1:
            results.append(
                FitResult(
                    fit_skill=get_fit_skill_from_name(fit_skill_box.name),
                    reps=get_reps_from_text(reps_candidate[0].name),
                )
            )
    return results



class FitResultOcrByVisionAPI(FitResultOcr):

    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def get_fit_result(self, image: FitResultImage):
        contents = vision.Image(content=image.raw_image)
        response =  self.client.document_text_detection(
            image=contents,
            image_context={'language_hints': ['ja']}
        )
        boxes = list_all_box(response)
        merged_box = merge_same_box(boxes)
        fit_result = get_fit_result(merged_box)
        return fit_result
