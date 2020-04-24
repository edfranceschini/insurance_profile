from domains.enums import OwnershipStatus, MaritalStatus
from domains import Auto, Home, Life, Disability


class Customer:
    def __init__(self,
                 age: int,
                 income: int,
                 dependents: int,
                 house: OwnershipStatus,
                 marital_status: MaritalStatus,
                 risk_questions: list,
                 vehicle_year: int
                 ):
        self.age = age
        self.income = income
        self.has_dependents = True if dependents > 0 else False
        self.house = house
        self.marital_status = marital_status
        self.risk_questions = risk_questions
        self.vehicle_year = vehicle_year


    def get_risk_profile(self):
        base_score = sum(self.risk_questions)
        auto = Auto(base_score, self.age, self.income, self.vehicle_year)
        life = Life(base_score, self.age, self.income, self.has_dependents, self.marital_status)
        home = Home(base_score, self.age, self.income, self.house)
        disability = Disability(base_score, self.age, self.income, self.marital_status, self.house, self.has_dependents)

        return [auto, disability, home, life]


