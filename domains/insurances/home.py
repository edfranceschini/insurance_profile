from domains.enums import OwnershipStatus, UserProfileStatus
from .insurance import Insurance


class Home(Insurance):
    def __init__(self, score: int, house_ownership_status: OwnershipStatus):
        self._score_ammount = 1
        super().__init__(score)
        self._update_profile(house_ownership_status)

    def _update_profile(self, house_ownership_status):
        if house_ownership_status == OwnershipStatus.HAS_NOT:
            self.profile = UserProfileStatus.INELIGIBLE
        elif house_ownership_status == OwnershipStatus.MORTGAGED:
            self.score += self._score_ammount
