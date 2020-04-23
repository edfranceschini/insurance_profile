from domains.enums.user_profile_status import UserProfileStatus


class Insurance:

    def __init__(self,
                 score: int,
                 age: int,
                 income: int):

        self.score = score
        self._profile = None

    @property
    def name(self):
        return type(self).__name__

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
