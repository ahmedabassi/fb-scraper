from sqlalchemy import Column , Integer, Text
from sqlalchemy.ext.declarative import declarative_base


Base  = declarative_base()

class FBPAGE(Base):
    __tablename__ = 'FBPAGE'
    id  = Column(Integer, primary_key=True, index=True)
    post_url = Column(Text)
    text = Column(Text)
    time = Column(Text) #change to DateTime
    image = Column(Text)
    likes = Column(Integer)
    comments = Column(Integer)
    shares = Column(Integer)

    