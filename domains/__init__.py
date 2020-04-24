from .insurances.insurance import Insurance
from .insurances.auto import Auto
from .insurances.home import Home
from .insurances.life import Life
from .insurances.disability import Disability
from .customers.customer import Customer

__all__ = [Insurance, Auto, Life, Home, Disability, Customer] #  TODO: verify if this is the right place for Customer
