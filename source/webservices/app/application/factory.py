from app.application.presentation.interfaces import IFactoryCommand
from app.application.persistence.interfaces import IFactoryContext
from app.domain.factory import Factory


class FactoryCommand(IFactoryCommand):

    def __init__( self, factory_context: IFactoryContext ):
        self.factory_context = factory_context

    def create_factory( self, phone: str, address: str ):
        factory = Factory()
        factory.phone = phone
        factory.set_address(address)

        self.factory_context.create_factory(factory)
