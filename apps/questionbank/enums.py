
from enum import StrEnum

class EducationLevelEnum(StrEnum):
    SIXTH_CLASS='SIXTH_CLASS'
    SEVENTH_CLASS='SEVENTH_CLASS'
    EIGHTH_CLASS='EIGHTH_CLASS'
    NINTH_CLASS='NINTH_CLASS'
    TENTH_CLASS='TENTH_CLASS'
    ELEVENTH_CLASS='ELEVENTH_CLASS'
    TWELFTH_CLASS='TWELFTH_CLASS'

    @classmethod
    def choices(cls):
        return [(r.value, r.name.title()) for r in cls]

class ExamTypeEnum(StrEnum):
    JEE='JEE'
    NEET='NEET'
    MHTCET='MHTCET'
    WBJEE='WBJEE'

    @classmethod
    def choices(cls):
        return [(r.value, r.name.title()) for r in cls]

class SubjectEnum(StrEnum):
    PHYSICS='PHYSICS'
    CHEMISTRY='CHEMISTRY'
    MATHEMATICS='MATHEMATICS'
    BIOLOGY='BIOLOGY'

    @classmethod
    def choices(cls):
        return [(r.value, r.name.title()) for r in cls]

class  QuestionTypeEnum(StrEnum):
    SINGLE_SELECT='SINGLE_SELECT'
    MULTI_SELECT='MULTI_SELECT'
    NUMERIC='NUMERIC'

    @classmethod
    def choices(cls):
        return [(r.value, r.name.title()) for r in cls]

class QuestionDifficultyLevelEnum(StrEnum):
    EASY='EASY'
    MEDIUM='MEDIUM'
    HARD='HARD'
    EXPERT='EXPERT'

    @classmethod
    def choices(cls):
        return [(r.value, r.name.title()) for r in cls]






