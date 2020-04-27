from domains import Insurance
from domains.enums import UserProfileStatus


class TestInsurance:

    def test_should_assert_economic_profile_when_score_below_zero(self):
        age = 35
        income = 0
        score = -2
        insurance = Insurance(score, age, income)

        assert insurance.profile == UserProfileStatus.ECONOMIC

    def test_should_assert_score_when_age_less_than_30_years(self):
        age = 25
        income = 0
        score = -2
        insurance = Insurance(score, age, income)

        assert insurance.score == -4

    def test_should_subtract_one_point_when_income_over_200k(self):
        age = 25
        income = 200001
        score = -2
        insurance = Insurance(score, age, income)

        assert insurance.score == -5

    def test_should_assert_profile_responsible_when_score_greater_than_2(self):
        age = 25
        income = 200001
        score = 6
        insurance = Insurance(score, age, income)

        assert insurance.profile == UserProfileStatus.RESPONSIBLE

    def test_should_assert_repr_when_profile_responsible(self):

        age = 25
        income = 0
        score = 6
        insurance = Insurance(score, age, income)
        format_expected = '<Insurance>: responsible, 4'

        assert insurance.__str__() == format_expected
