from domains import Auto
from domains.enums.user_profile_status import UserProfileStatus
from datetime import datetime as dt


class TestAuto:
    def test_should_assert_score_when_auto_year_is_less_than_5_years(self):
        age = 40
        income = 0
        auto_year = dt.today().year - 4
        score = 4

        auto = Auto(score, age, income, auto_year)

        assert auto.score == 4

    def test_should_assert_ineligible_when_auto_year_equals_zero(self):
        age = 40
        income = 0
        auto_year = 0
        score = 4

        auto = Auto(score, age, income, auto_year)

        assert auto.profile == UserProfileStatus.INELIGIBLE

    def test_should_assert_score_when_auto_year_is_greater_than_5_years(self):
        age = 40
        income = 0
        auto_year = dt.today().year - 6
        score = 1

        auto = Auto(score, age, income, auto_year)

        assert auto.score == 0
