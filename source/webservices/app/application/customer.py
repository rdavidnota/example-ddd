from app.application.presentation.interfaces import ICustomerCommand
from app.domain.customer import Customer as DomainCustomer
from app.application.persistence.interfaces import ICustomerContext


class CustomerCommand(ICustomerCommand):

    def __init__(self, customer_context: ICustomerContext):
        self.customer_context = customer_context

    def save_customer(self, name):
        customer = DomainCustomer()
        customer.name = name

        self.customer_context.save_customer(customer)

    def list_customer(self):
        customers = self.customer_context.list_customers()
        return customers
