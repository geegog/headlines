import datetime
from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship

from headlines.database import Base

from headlines.models.newpaper import Company

from headlines.models.categories import Category


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    headline = Column(String(500), unique=True)
    link = Column(String(50), unique=True)
    created = Column(DATETIME())
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    def __init__(self, headline=None, link=None, created=datetime.datetime.now(), company_id=None, category_id=None):
        self.headline = headline
        self.link = link
        self.created = created
        self.company_id = company_id
        self.category_id = category_id

    def serialize(self):
        return {
            'id': self.id,
            'headline': self.headline,
            'link': self.link,
            'created': self.created,
            'company': self.company,
            'category': self.category
        }

    def __repr__(self):
        return '<Link %r>' % self.link
