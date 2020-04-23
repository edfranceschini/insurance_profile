from domains import UserProfileStatus, Insurance


class TestInsurance:

    def test_should_assert_economic_profile_when_score_below_zero(self):
        score = -2
        age = 26
        income = 10
        insurance = Insurance(score, age, income)

        assert UserProfileStatus.ECONOMIC == insurance.profile


