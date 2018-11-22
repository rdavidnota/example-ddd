from app.domain.factory import Factory as FactoryDomain
from app.persistence.entities.models import Factory
from app.persistence import session
from app.application.persistence.interfaces import IFactoryContext


class FactoryContext(IFactoryContext):

    def create_factory( self, factory: FactoryDomain ):
        persistence_factory = Factory()

        persistence_factory.phone = factory.phone
        persistence_factory.address = factory.get_address()

        session.add(persistence_factory)
        session.commit()
