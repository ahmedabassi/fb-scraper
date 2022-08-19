from sqlalchemy import Column , Integer, String ,DateTime
from sqlalchemy.ext.declarative import declarative_base


Base  = declarative_base()

class FBPAGE(Base):
    __tablename__ = 'FBPAGE'
    id  = Column(Integer, primary_key=True, index=True)
    post_url = Column(String(4096))
    text = Column(String(4096))
    time = Column(String(4096)) #change to DateTime
    image = Column(String(4096))
    likes = Column(Integer)
    comments = Column(Integer)
    shares = Column(Integer)

    