from domains.enums import UserProfileStatus, OwnershipStatus
from domains import Home

class TestHome:

    def test_should_assert_ineligible_when_has_not_hom(self):
        score = 0
        home = Home(score, OwnershipStatus.HAS_NOT)

        assert home.profile == UserProfileStatus.INELIGIBLE

    def test_should_assert_score_when_home_ownership_is_mortaged(self):
        score = 0
        home = Home(score, OwnershipStatus.MORTGAGED)

        assert home.score == 1
