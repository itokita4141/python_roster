# 参考 https://qiita.com/Edim/items/90ee83a5d385807f67a6

from .models import Users, Attendances, Log
from app_roster import serializers

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['name', 'age']

class AttendancesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendances
        fields = ['title', 'description', 'author']

class Logs(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Logs
        fields = ['title', 'description', 'author']