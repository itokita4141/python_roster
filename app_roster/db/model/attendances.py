import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
sys.path.append("../config")
from setting_alchemy import Base
from setting_alchemy import ENGINE
import datetime
from sqlalchemy import (Text, Time, Boolean)

class Attenances(Base):
    # """
    # ユーザモデル
    # """
    __tablename__ = 'attenances'
    attendanceId = Column('attendanceId', Integer, primary_key=True)
    userId = Column('userId', Integer)
    yearMonth = Column('yearMonth', String(6), nullable=False)
    day = Column('day', String(2), nullable=False)
    startTime = Column('startTime', Time)
    dndDateTime = Column('endDateTime', DateTime)
    restStartTime = Column('restStartTime', DateTime)
    restEndTime = Column('restEndTime', DateTime)
    deleteFlag = Column('deleteFlag', Boolean, default=0)
    updateTIme = Column('updateTime', DateTime)
    addTime = Column('addTime', DateTime)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)