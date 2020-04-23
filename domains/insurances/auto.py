from datetime import datetime as dt
from .insurance import Insurance, UserProfileStatus


class Auto(Insurance):

    def __init__(self, auto_year: int, score: int, age: int, income: int):
        self._years_to_date = 5
        self.auto_year = auto_year
        self._score_ammount = 1
        super().__init__(score, age, income)
        self.update_score()

    def update_score(self):
        if self.auto_year == 0:
            self.profile = UserProfileStatus.INELIGIBLE
        elif self.auto_year >= (dt.now().year - self._years_to_date):
            self.score += self._score_ammount
