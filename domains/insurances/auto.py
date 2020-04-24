from datetime import datetime as dt

from domains.enums import UserProfileStatus

from .insurance import Insurance


class Auto(Insurance):

    def __init__(self, score: int, age: int, income: int, auto_year: int):
        self._years_to_date = 5
        self.auto_year = auto_year
        self._score_amount = 1
        super().__init__(score, age, income)
        self._update_profile()

    def _update_profile(self):
        vehicle_is_eligible = self.auto_year >= (dt.now().year - self._years_to_date)
        if self.auto_year == 0:
            self.profile = UserProfileStatus.INELIGIBLE
        if vehicle_is_eligible:
            self.score += self._score_amount
