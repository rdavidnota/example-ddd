from app.persistence.customer import CustomerContext
from app.application.customer import CustomerCommand

from app.persistence.factory import FactoryContext
from app.application.factory import FactoryCommand


class Factory:

    @staticmethod
    def create_customer_command():
        customer_context = CustomerContext()
        customer_command = CustomerCommand(customer_context)
        return customer_command

    @staticmethod
    def create_factory_command():
        factory_context = FactoryContext()
        factory_command = FactoryCommand(factory_context)
        return factory_command
