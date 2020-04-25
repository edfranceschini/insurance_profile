from pydantic import BaseModel, Field


class Auto(BaseModel):
    year: int = Field(
        ...,
        gt=0)
