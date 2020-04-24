from .insurance import Insurance
from domains.enums import MaritalStatus, OwnershipStatus, UserProfileStatus


class Disability(Insurance):

    def __init__(self,
                 score: int,
                 age: int,
                 income: int,
                 marital_status: MaritalStatus,
                 house: OwnershipStatus,
                 has_dependents: bool):
        super().__init__(score)
        self._score_amount = 1
        self._update_profile(age, income, house, marital_status, has_dependents)

    def _update_profile(self,
                        age,
                        income,
                        house,
                        marital_status,
                        has_dependents):
        if income == 0 or age > 60:
            self.profile = UserProfileStatus.INELIGIBLE
        if OwnershipStatus.MORTGAGED == house or has_dependents:
            self.score += self._score_amount
        if MaritalStatus.MARRIED == marital_status:
            self.score -= self._score_amount
