from domains.enums import UserProfileStatus, OwnershipStatus
from domains import Home

class TestHome:

    def test_should_assert_ineligible_when_has_not_home(self):
        age = 35
        income = 0
        score = 1
        home = Home(score, age, income, OwnershipStatus.HAS_NOT)

        assert home.profile == UserProfileStatus.INELIGIBLE

    def test_should_assert_score_when_home_ownership_is_mortgaged(self):
        age = 35
        income = 0
        score = 1
        home = Home(score, age, income, OwnershipStatus.MORTGAGED)

        assert home.score == 1
