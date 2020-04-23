from domains.insurances.auto import Auto
from domains.enums.user_profile_status import UserProfileStatus
from datetime import datetime as dt


class TestAuto:
    def test_should_assert_score_when_auto_year_is_less_than_5_years(self):
        auto_year = dt.today().year - 4
        score = 0
        age = 26
        income = 0

        auto = Auto(auto_year, score, age, income)

        assert auto.score == 1

    def test_should_assert_ineligible_when_auto_year_equals_zero(self):
        auto_year = 0
        score = 0
        age = 26
        income = 0

        auto = Auto(auto_year, score, age, income)

        assert auto.profile == UserProfileStatus.INELIGIBLE

    def test_should_assert_score_when_auto_year_is_greater_than_5_years(self):
        auto_year = dt.today().year - 6
        score = 0
        age = 26
        income = 0

        auto = Auto(auto_year, score, age, income)

        assert auto.score == 0