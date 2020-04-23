from domains import UserProfileStatus, Insurance


class TestInsurance:

    def test_should_return_economic_profile_when_score_below_zero(self):
        score = -2
        insurance = Insurance(score)

        assert UserProfileStatus.ECONOMIC == insurance.profile
