import datetime
from sqlalchemy import Column, Integer, String, DATETIME

from headlines.database import Base
from sqlalchemy.orm import relationship


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    created = Column(DATETIME())
    email = Column(String(50), unique=True)
    news = relationship("News")

    def __init__(self, name=None, email=None, created=datetime.datetime.now()):
        self.name = name
        self.email = email
        self.created = created

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created': self.created
        }

    def __repr__(self):
        return 'User %r>' % self.name

