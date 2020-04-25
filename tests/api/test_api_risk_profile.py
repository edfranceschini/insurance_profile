from starlette.testclient import TestClient
from main import app
import pytest

INELIGIBLE = 'ineligible'
ERROR_STATUS_CODE = 422


class TestApiUser:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.client = TestClient(app)
        self.url = '/'

    def test_should_assert_age_equal_to_or_greater_than_zero(self):
        input_data = {
            'age': -7,
            'dependents': 2,
            'income': 0,
            'marital_status': 'married',
            'risk_questions': [0, 1, 0]
        }

        response = self.client.post(self.url, json=input_data)
        assert response.status_code == ERROR_STATUS_CODE

    def test_should_assert_dependents_equal_to_or_greater_than_zero(self):
        input_data = {
            'age': 20,
            'dependents': -2,
            'income': 0,
            'marital_status': 'married',
            'risk_questions': [0, 1, 0]
        }

        response = self.client.post(self.url, json=input_data)
        assert response.status_code == ERROR_STATUS_CODE

    def test_should_assert_ineligible_auto_insurance_when_customer_has_no_vehicle(self):
        input_data = {
            'age': 26,
            'dependents': 1,
            'income': 0,
            'marital_status': 'single',
            'risk_questions': [1, 1, 0]
        }
        auto_profile_expected = INELIGIBLE

        response = self.client.post(self.url, json=input_data).json()
        assert auto_profile_expected == response['auto']

    def test_should_assert_ineligible_home_insurance_when_customer_has_no_home(self):
        input_data = {
            'age': 26,
            'dependents': 2,
            'income': 0,
            'marital_status': 'married',
            'risk_questions': [0, 1, 0]
        }
        home_profile_expected = INELIGIBLE

        response = self.client.post(self.url, json=input_data).json()
        assert home_profile_expected == response['home']

    def test_should_assert_income_equal_to_or_greater_than_zero(self):
        input_data = {
            'age': 26,
            'dependents': 1,
            'income': -1000,
            'marital_status': 'married',
            'risk_questions': [0, 1, 0]
        }

        response = self.client.post(self.url, json=input_data)
        assert response.status_code == ERROR_STATUS_CODE

    def test_should_assert_marital_status(self):
        input_data = {
            'age': 26,
            'dependents': 1,
            'income': 0,
            'marital_status': 'divorced',
            'risk_questions': [0, 1, 0]
        }

        response = self.client.post(self.url, json=input_data)
        assert response.status_code == ERROR_STATUS_CODE

    def test_should_assert_risk_questions_array_length(self):
        input_data = {
            'age': 26,
            'dependents': 1,
            'income': 0,
            'marital_status': 'married',
            'risk_questions': [0, 1, 0, 1]
        }

        response = self.client.post(self.url, json=input_data)
        assert response.status_code == ERROR_STATUS_CODE

    def test_should_validate_risk_questions_value_range_from_0_to_1(self):
        input_data = {
            'age': 26,
            'dependents': 0,
            'income': 0,
            'marital_status': 'single',
            'risk_questions': [0, 2, 1]
        }

        response = self.client.post(self.url, json=input_data)
        assert response.status_code == ERROR_STATUS_CODE
