from enum import Enum


class OwnershipStatus(Enum):
    HAS_NOT = ''
    OWNED = 'owned'
    MORTGAGED = 'mortgaged'
