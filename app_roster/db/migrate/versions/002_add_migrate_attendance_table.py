from sqlalchemy import *
from migrate import *
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME, TEXT
# TIMESTAMP用
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp

meta = MetaData()
attendance_table = Table(
    'migrate_attendance', meta,
    Column('attendanceId', BIGINT(unsigned=True), primary_key=True),
    Column('userId', BIGINT(unsigned=True)),
    Column('yearMonth', VARCHAR(6), nullable=False),
    Column('day', VARCHAR(2), nullable=False),
    Column('startTime', TIMESTAMP),
    Column('endDateTime', TIMESTAMP),
    Column('restStartTime', TIMESTAMP),
    Column('restEndTime', TIMESTAMP),
    Column('deleteFlag', BOOLEAN, default=0),
    Column('updateTime', TIMESTAMP),
    Column('addTime', TIMESTAMP, server_default=current_timestamp()))

# attendanceId = models.IntegerField(null=False, blank=False, primary_key=True, verbose_name="出勤ID")
# userId = models.IntegerField(null=False, blank=False, verbose_name="ユーザーID")
# yearMonth = models.CharField(max_length=6, null=True, blank=True, verbose_name="対象年月")
# day = models.CharField(max_length=2, null=True, blank=True, verbose_name="対象日")
# startTime = models.CharField(max_length=8, blank=True, null=True, verbose_name="勤務開始時間")
# endDateTime = models.DateTimeField(blank=True, null=True, verbose_name="勤務終了時間")
# restStartTime = models.DateTimeField(blank=True, null=True, verbose_name="休憩開始時間")
# restEndTime = models.DateTimeField(blank=True, null=True, verbose_name="休憩終了時間")
# deleteFlag = models.BooleanField(default=True, verbose_name="削除フラグ")
# updateTime = models.DateTimeField(blank=True, null=True, default=timezone.now, verbose_name="更新時間")
# addTime = models.DateTimeField(blank=True, null=True, default=timezone.now, verbose_name="追加時間")

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    attendance_table.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    attendance_table.drop()
