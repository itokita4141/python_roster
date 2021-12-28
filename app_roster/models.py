# from django.db import models
from djongo import models


class Users(models.Model):
    userId = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),
    name = models.CharField(max_length=20),
    address = models.CharField(max_length=100),
    tell = models.CharField(max_length=20),
    sex = models.CharField(max_length=1),
    contract = models.CharField(max_length=20),
    email = models.CharField(max_length=20),
    password = models.CharField(max_length=10),
    deleteFlag = models.BooleanField(default=False),
    updateTime = models.DateField(null=False),
    addTime = models.BooleanField(null=True),

    def __str__(self):
        return str(self.__dict__)

class Attendance(models.Model):
    attendanceId = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),
    userId = models.BigIntegerField(),
    yearMonth = models.CharField(max_length=6),
    day = models.CharField(max_length=2),
    startTime = models.DateTimeField(),
    endDateTime = models.DateTimeField(),
    restStartTime = models.DateTimeField(),
    restEndTime = models.DateTimeField(),
    deleteFlag = models.BooleanField(default=False),
    updateTime = models.DateField(null=False),
    addTime = models.BooleanField(null=True),

    def __str__(self):
        return str(self.__dict__)

