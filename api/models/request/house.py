from pydantic import BaseModel
from domains.enums import OwnershipStatus


class House(BaseModel):
    ownership_status: OwnershipStatus
