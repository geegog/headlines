from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class News(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    created = Column(DATETIME())
    news_id = Column(Integer, ForeignKey('news.id'), nullable=False)

    news = relationship("News", back_populates="categories")

    def __init__(self, name=None, created=None, news_id=None):
        self.name = name
        self.created = created
        self.news_id = news_id

    def __repr__(self):
        return '<Name %r>' % self.name

