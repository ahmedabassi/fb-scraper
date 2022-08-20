from sqlalchemy import Column , Integer, String ,DateTime , VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base  = declarative_base()

class FBPAGE(Base):
    __tablename__ = 'FBPAGE'
    id  = Column(Integer, primary_key=True, index=True)
    post_url = Column(VARCHAR(1024))
    text = Column(VARCHAR(1024))
    time = Column(VARCHAR(1024)) #change to DateTime
    image = Column(VARCHAR(1024))
    likes = Column(Integer)
    comments = Column(Integer)
    shares = Column(Integer)

    