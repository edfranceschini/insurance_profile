from domains.enums import OwnershipStatus, MaritalStatus
from domains import Auto, Home, Life, Disability


class Customer:
    def __init__(self,
                 age: int,
                 income: int,
                 dependents: int,
                 house: OwnershipStatus,
                 marital_stats: MaritalStatus,
                 risk_questions: list,
                 vehicle_year: int
                 ):
        self.age = age
        self.income = income
        self.has_dependents = True if dependents > 0 else False
        self.house = house
        self.marital_status = MaritalStatus
        self.risk_questions = risk_questions
        self.vehicle_year = vehicle_year


    def get_risk_profile(self):
        base_score = sum(self.risk_questions)
        auto = Auto(base_score, self.vehicle_year)
        return []

