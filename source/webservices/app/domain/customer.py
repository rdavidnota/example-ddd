from app.domain.base import Base


class Customer(Base):

    def __init__(self):
        self.name = ""

    def to_json(self):
        return {'name': self.name, 'id': self.id}
