from domains import Disability
from domains.enums import MaritalStatus, OwnershipStatus, UserProfileStatus


class TestDisabilitry:

    def test_should_assert_ineligible_when_user_has_no_income(self):
        age = 23
        income = 0
        score = 0
        house = OwnershipStatus.MORTGAGED
        marital_status = MaritalStatus.MARRIED
        has_dependents = True

        disability = Disability(score, age, income, marital_status, house, has_dependents)

        assert disability.profile == UserProfileStatus.INELIGIBLE
