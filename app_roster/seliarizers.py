# 参考 https://qiita.com/Edim/items/90ee83a5d385807f67a6

from .models import Users, Attendances, Logs
from rest_framework import serializers

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        # fields = ['name']
        fields = ['id','userId','name','address','tell','sex',
                  'contract','email','password','deleteFlag',
                  'updateTime','addTime']
        # read_only_fields = ('id',)

class AttendancesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendances
        fields = ['id','attendanceId','userId','yearMonth',
                  'day','startTime','endDateTime','restStartTime',
                  'restEndTime','deleteFlag','updateTime','addTime']
        # read_only_fields = ('id',)

class LogsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Logs
        fields = ['id','logId','userId','content',
                  'deleteFlag','updateTime','addTime']
        # read_only_fields = ('id',)

