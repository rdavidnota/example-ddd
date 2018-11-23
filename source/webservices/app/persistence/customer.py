from app.domain.customer import Customer as DomainCustomer
from app.persistence.entities.models import Customer
from app.persistence import session
from app.application.persistence.interfaces import ICustomerContext


class CustomerContext(ICustomerContext):

    def save_customer(self, customer: DomainCustomer):
        persistence_customer = Customer()
        persistence_customer.name = customer.name
        session.add(persistence_customer)
        session.commit()

    def list_customers(self):
        customers = []
        for customer in session.query(Customer).all():
            domain_customer = DomainCustomer()
            domain_customer.id = customer.id
            domain_customer.name = customer.name
            customers.append(domain_customer)
        return customers
