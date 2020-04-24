from .insurance import Insurance
from domains.enums import UserProfileStatus, MaritalStatus


class Life(Insurance):
    def __init__(self, score, age: int, has_dependents: bool, marital_status: MaritalStatus):
        self._score_amount = 1
        super().__init__(score)
        self._update_profile(age, has_dependents, marital_status)

    def _update_profile(self, age, has_dependents, marital_status):
        if marital_status == MaritalStatus.MARRIED:
            self.score += self._score_amount
        if age > 60:
            self.profile = UserProfileStatus.INELIGIBLE
        if has_dependents:
            self.score += self._score_amount
