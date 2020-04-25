from pydantic import BaseModel


class InsuranceStatus(BaseModel):
    auto: str
    disability: str
    home: str
    life: str
