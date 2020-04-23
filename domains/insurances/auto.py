from datetime import datetime as dt

from domains.enums import UserProfileStatus

from .insurance import Insurance


class Auto(Insurance):

    def __init__(self, auto_year: int, score: int):
        self._years_to_date = 5
        self.auto_year = auto_year
        self._score_ammount = 1
        super().__init__(score)
        self._update_profile()

    def _update_profile(self):
        if self.auto_year == 0:
            self.profile = UserProfileStatus.INELIGIBLE
        elif self.auto_year >= (dt.now().year - self._years_to_date):
            self.score += self._score_ammount
