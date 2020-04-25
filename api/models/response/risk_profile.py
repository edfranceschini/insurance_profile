from pydantic import BaseModel


class RiskProfile(BaseModel):
    auto: str
    disability: str
    home: str
    life: str
