from fastapi import APIRouter
from .models import RiskProfile, Customer as CustomerRequest

from domains.enums import OwnershipStatus
from domains import Customer

router = APIRouter()


@router.post('/', response_model=RiskProfile)
def risk_profile(customer_request: CustomerRequest) -> RiskProfile:
    customer = customer_input_mapper(customer_request)
    profile = customer.get_risk_profile()
    risk_mapped = {risk.name.lower(): risk.profile.value for risk in profile}
    return RiskProfile(**risk_mapped)


def customer_input_mapper(customer_request: CustomerRequest) -> Customer:
    house_status = customer_request.house.ownership_status if customer_request.house else OwnershipStatus.HAS_NOT
    year_vehicle = customer_request.vehicle.year if customer_request.vehicle else 0
    return Customer(customer_request.age,
                    customer_request.income,
                    customer_request.dependents,
                    house_status,
                    customer_request.marital_status,
                    customer_request.risk_questions,
                    year_vehicle
                    )
