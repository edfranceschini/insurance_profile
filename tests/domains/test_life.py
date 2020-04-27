from domains.enums import MaritalStatus, UserProfileStatus
from domains import Life


class TestLife:

    def test_should_assert_score_when_user_has_dependents(self):
        score = 2
        has_dependents = True
        age = 20
        income = 0
        marital_status = MaritalStatus.SINGLE

        life = Life(score, age, income, has_dependents, marital_status)
        assert life.score == 1

    def test_should_assert_score_when_user_is_married(self):
        score = 2
        has_dependents = False
        age = 20
        income = 0
        marital_status = MaritalStatus.MARRIED

        life = Life(score, age, income, has_dependents, marital_status)
        assert life.score == 1

    def test_should_assert_score_when_user_is_married_and_has_dependents(self):
        score = 2
        has_dependents = True
        age = 20
        income = 0
        marital_status = MaritalStatus.MARRIED

        life = Life(score, age, income, has_dependents, marital_status)
        assert life.score == 2

    def test_should_assert_profile_ineligible_when_age_grater_than_60(self):
        score = 2
        has_dependents = True
        age = 61
        income = 0
        marital_status = MaritalStatus.MARRIED

        life = Life(score, age, income, has_dependents, marital_status)
        assert life.profile == UserProfileStatus.INELIGIBLE
