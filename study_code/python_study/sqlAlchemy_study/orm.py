from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Account(Base):
    __tablename__ = u'account'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    title = Column(String(50))
    salary = Column(Integer)

    def is_active(self):
        # for example all the account is active
        return True

    def get_id(self):
        # return accound ID, improve the package characties user the method return proprety
        return self.id

    def is_authenticated(self):
        # Assume has paas the verification
        return True

    def is_anonymous(self):
        # has the login name and paaswoed is not the anonymous user
        return False

class Bulltin(Base):
    __tablename__ = 'bulltin'

    id = Column(Integer, primary_key=True)
    dt = Column(String(200), nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(String(200), nullable=False)
    valid = Column(String(200), nullable=False)
    source = Column(String(200), nullable=False)
    author = Column(String(50), nullable=False)
    image = Column(String(200), nullable=False)