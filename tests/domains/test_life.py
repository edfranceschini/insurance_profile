from domains.enums import MaritalStatus
from domains import Life


class TestLife:

    def test_should_assert_score_when_user_has_dependents(self):
        score = 0
        has_dependents = True
        age = 20
        marital_status = MaritalStatus.SINGLE

        life = Life(score, age, has_dependents, marital_status)
        assert life.score == 1

    def test_should_assert_score_when_user_is_married(self):
        score = 0
        has_dependents = False
        age = 20
        marital_status = MaritalStatus.MARRIED

        life = Life(score, age, has_dependents, marital_status)
        assert life.score == 1

    def test_should_assert_score_when_user_is_married_and_has_dependents(self):
        score = 0
        has_dependents = True
        age = 20
        marital_status = MaritalStatus.MARRIED

        life = Life(score, age, has_dependents, marital_status)
        assert life.score == 2
