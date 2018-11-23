from abc import ABC, abstractmethod
from app.domain.customer import Customer as DomainCustomer
from app.domain.factory import Factory as DomainFactory


class ICustomerContext(ABC):

    @abstractmethod
    def save_customer(self, customer: DomainCustomer):
        pass

    @abstractmethod
    def list_customers(self):
        pass


class IFactoryContext(ABC):

    @abstractmethod
    def create_factory(self, factory: DomainFactory):
        pass

    @abstractmethod
    def list_factories(self):
        pass
