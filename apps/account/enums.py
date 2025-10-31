from enum import StrEnum

class RoleEnum(StrEnum):
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = "ADMIN"
    USER = "USER"
    SME  = "SME"

    @classmethod
    def choices(cls):
        return [(r.value, r.name.title()) for r in cls]
