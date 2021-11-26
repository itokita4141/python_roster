from sqlalchemy import *
from migrate import *
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME, TEXT
# TIMESTAMP用
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp

meta = MetaData()
table = Table(
    'migrate_users', meta,
    Column('userId', BIGINT(unsigned=True), primary_key=True),
    Column('name', TEXT, nullable=False),
    Column('address', VARCHAR(64), nullable=False),
    Column('tell', VARCHAR(64), nullable=False),
    Column('sex', VARCHAR(64), nullable=False),
    Column('contract', VARCHAR(64), nullable=False),
    Column('deleteFlag', BOOLEAN, default=0),
    Column('updateTime', TIMESTAMP),
    Column('addTime', TIMESTAMP, server_default=current_timestamp()))

# userId = models.IntegerField(null=False, blank=False, primary_key=True, verbose_name="ユーザーID")
# name = models.CharField(max_length=20, verbose_name="名前")
# address = models.CharField(max_length=100, verbose_name="住所")
# tell = models.CharField(max_length=20, null=True, blank=True, verbose_name="電話番号")
# sex = models.CharField(max_length=1, verbose_name="性別(m:男性,f:女性)")
# contract = models.CharField(max_length=100, null=False, blank=False, verbose_name="社員パートなど")
# deleteFlag = models.BooleanField(default=True, verbose_name="削除フラグ")
# updateTime = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="更新日時")
# addTime = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="追加日時")


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    table.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    table.drop()
