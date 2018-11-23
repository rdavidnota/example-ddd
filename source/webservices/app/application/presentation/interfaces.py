from abc import ABC, abstractmethod


class ICustomerCommand(ABC):

    @abstractmethod
    def save_customer(self, name):
        pass

    @abstractmethod
    def list_customer(self):
        pass


class IFactoryCommand(ABC):

    @abstractmethod
    def create_factory(self, phone: str, address: str):
        pass

    @abstractmethod
    def list_factories(self):
        pass
