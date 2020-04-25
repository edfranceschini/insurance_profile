from datetime import datetime as dt
from domains.enums import UserProfileStatus
from domains import Customer


class TestCustomer:

    def test_should_assert_risk_profile(self):
        age = 35
        income = 0
        dependents = 2
        house = 'owned'
        marital_status = 'married'
        risk_questions = [0, 1, 0]
        vehicle_year = dt.now().year - 2

        auto_profile_expected = UserProfileStatus.REGULAR
        disability_profile_expected = UserProfileStatus.INELIGIBLE
        home_profile_expected = UserProfileStatus.ECONOMIC
        life_profile_expected = UserProfileStatus.REGULAR

        errors = []

        customer_insurances = Customer(
            age,
            income,
            dependents,
            house,
            marital_status,
            risk_questions,
            vehicle_year
        ).get_risk_profile()

        for insurance in customer_insurances:
            if insurance.name == 'Auto' and insurance.profile != auto_profile_expected:
                errors.append('Auto')
            elif insurance.name == 'Disability' and insurance.profile != disability_profile_expected:
                errors.append('Disability')
            elif insurance.name == 'Home' and insurance.profile != home_profile_expected:
                errors.append('Home')
            elif insurance.name == 'Life' and insurance.profile != life_profile_expected:
                errors.append('Life')

        assert len(errors) == 0
