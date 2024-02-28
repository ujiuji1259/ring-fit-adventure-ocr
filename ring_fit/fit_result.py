import re
from dataclasses import dataclass
from datetime import date

from ring_fit.fit_skill import FitSkill, get_fit_skill_from_name


@dataclass
class FitResult:
    fit_skill: FitSkill
    reps: int
