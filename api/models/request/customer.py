from .house import House
from .auto import Auto
from domains.enums import MaritalStatus
from pydantic import BaseModel, Field, validator


class Customer(BaseModel):
    age: int = Field(
        ...,
        ge=0)
    dependents: int = Field(
        ...,
        ge=0)
    house: House = None
    income: int = Field(
        ...,
        ge=0)
    marital_status: MaritalStatus
    risk_questions: list
    vehicle: Auto = None

    class Config:
        schema_extra = {
            'example': {
                'age': 26,
                'dependents': 0,
                'house': {'ownership_status': 'mortgaged'},
                'income': 0,
                'marital_status': 'married',
                'risk_questions': [0, 1, 0],
                'vehicle': {'year': 2018}
            }
        }

    @validator('risk_questions')
    def risk_questions_validator(cls, risk_questions):
        if len(risk_questions) != 3 or [question for question in risk_questions if question > 1]:
            raise ValueError('Incorrect format for risk_questions field')
        return risk_questions
