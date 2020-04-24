from domains.enums import UserProfileStatus


class Insurance:

    def __init__(self, score: int, age: int, income: int):
        self.age = age
        self.income = income
        self._score = score
        self._profile = None
        self.income_threshold_good = 200000

    @property
    def name(self):
        return type(self).__name__

    @property
    def score(self):
        # Age all lines deduction
        if self.age < 30:
            self._score -= 2
        elif self.age > 30 < 40:
            self._score -= 1

        # Income all lines deduction
        if self.income > self.income_threshold_good:
            self._score -= 1

        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def profile(self):
        if self._profile != UserProfileStatus.INELIGIBLE:
            if self.score <= 0:
                self._profile = UserProfileStatus.ECONOMIC
            elif 1 <= self.score <= 2:
                self._profile = UserProfileStatus.REGULAR
            else:
                self._profile = UserProfileStatus.RESPONSIBLE
        return self._profile

    @profile.setter
    def profile(self, profile):
        self._profile = profile

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'<{self.name}>: {self.profile.value}, {self.score}'
