from app.domain.base import Base


class Customer(Base):

    def __init__(self):
        self.name = ""

    def toJSON(self):
        return {'name': self.name, 'id': self.id}
