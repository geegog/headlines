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

    company = relationship("Company", back_populates="news")

    def __init__(self, headline=None, link=None, created=None, company_id=None):
        self.headline = headline
        self.link = link
        self.created = created
        self.company_id = company_id

    def __repr__(self):
        return '<Link %r>' % self.link

