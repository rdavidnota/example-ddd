from app.persistence.entities.models import Customer
from app.persistence import session


def SaveCustomer():
    customer = Customer()
    customer.name = "test"
    session.add(customer)
    session.commit()
