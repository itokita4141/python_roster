import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import (Text, Time, Boolean)
sys.path.append("../config")
from setting_alchemy import Base
from setting_alchemy import ENGINE

class Users(Base):
    __tablename__ = 'users'
    userId = Column('userId', Integer, primary_key=True)
    name = Column('name', String(20), nullable=False)
    address = Column('address', String(64), nullable=False)
    tell = Column('tell', String(64), nullable=False)
    sex = Column('sex', String(64), nullable=False)
    contract = Column('contract', String(64), nullable=False)
    deleteFlag = Column('deleteFlag', Boolean, default=0)
    updateTime = Column('updateTime', DateTime)
    addTime = Column('addTime', DateTime)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)