from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# postgresql
# rrkwiepojqjmww
# 172d2d30c807aeca359c780861f63bcaa276bd8b9c25e2e6444ab6b8ec5dbf2c
# ec2-35-172-16-31.compute-1.amazonaws.com:5432
# de5q7mpd4qi77e

# mysqlのDBの設定
DATABASE = 'postgresql://%s:%s@%s/%s' % (
    "rrkwiepojqjmww",
    "172d2d30c807aeca359c780861f63bcaa276bd8b9c25e2e6444ab6b8ec5dbf2c",
    "ec2-35-172-16-31.compute-1.amazonaws.com:5432",
    "de5q7mpd4qi77e",
)
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True # Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
session = scoped_session(
  # ORM実行時の設定。自動コミットするか、自動反映するなど。
        sessionmaker(
                autocommit = False,
                autoflush = False,
                bind = ENGINE
        )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()