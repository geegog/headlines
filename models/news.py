import datetime
from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    headline = Column(String(500))
    link = Column(String(50))
    created = Column(DATETIME())
    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    company = relationship("Company", back_populates="news")
    category = relationship("Category", back_populates="news")

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
            'company_id': self.company_id,
            'category_id': self.category_id
        }

    def __repr__(self):
        return '<Link %r>' % self.link

