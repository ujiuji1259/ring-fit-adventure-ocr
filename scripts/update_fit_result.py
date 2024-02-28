import os
from datetime import date, datetime

from fire import Fire

from ring_fit.image_downloader import FitResultImageDownloader
from ring_fit.ocr.vision_api import FitResultOcrByVisionAPI
from ring_fit.fit_result_updater import FitSkillUpdater


DRIVE_ID = os.environ['DRIVE_ID']
SHEET_ID = os.environ['SHEET_ID']
SHEET_NAME = os.environ['SHEET_NAME']


def main(from_date: date, to_date: date):
    downloader = FitResultImageDownloader(DRIVE_ID)
    ocr = FitResultOcrByVisionAPI()
    updater = FitSkillUpdater(sheet_id=SHEET_ID, sheet_name=SHEET_NAME)
    images = downloader.download_images(
        datetime.strptime(from_date, '%Y-%m-%d').date(),
        datetime.strptime(to_date, '%Y-%m-%d').date(),
    )

    for image in images:
        fit_result = ocr.get_fit_result(image)
        updater.append(fit_result, image.actioned_at)


if __name__ == '__main__':
    Fire(main)
