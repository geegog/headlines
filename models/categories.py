import datetime
from sqlalchemy import Column, Integer, String, DATETIME

from headlines.database import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    created = Column(DATETIME())

    def __init__(self, name=None, created=datetime.datetime.now()):
        self.name = name
        self.created = created

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'created': self.created,
        }

    def __repr__(self):
        return '<Name %r>' % self.name

