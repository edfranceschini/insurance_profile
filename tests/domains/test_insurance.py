from domains import Insurance
from domains.enums import UserProfileStatus


class TestInsurance:

    def test_should_assert_economic_profile_when_score_below_zero(self):
        age = 35
        income = 0
        score = -2
        insurance = Insurance(score, age, income)

        assert UserProfileStatus.ECONOMIC == insurance.profile
