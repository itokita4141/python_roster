# 参考 https://qiita.com/Edim/items/90ee83a5d385807f67a6

from .models import Users, Attendances, Logs
from .models import umaCardMaster, umaCardSkillMaster, umaCardMessageMaster, umaWhiteFactor

from rest_framework import serializers
# うま用

# class umaCardMasterSerializer(serializers.HyperlinkedModelSerializer):
#     class META:
#         model = umaCardMaster
#         fields = {
#             'id', 'cardMasterId', 'limitedOverNum', 'cardId', 'cardTypeNo',
#             'cardTypeName', 'cardName', 'rared', 'specialityRare', 'yarukiEffect',
#             'friendlyBonus', 'trainingEffect', 'speedBonus', 'staminaBonus', 'powerBonus',
#             'skillBonus', 'gutsBonus', 'wiseBonus', 'wiseBonus100', 'hintLevel',
#             'hintIncidence', 'defaultKizunaGage', 'defaultSpeed', 'defaultStamina', 'defaultPower',
#             'defaultWise', 'defaultGuts', 'raceBonus', 'fanNumber_Bonus', 'trainingEffect',
#             'eventEffect', 'wiseFriendlyRecoverlyAmount', 'eventRecoveryAmont', 'lifeComsumptionDown',
#             'failureRateDown',
#             'ura_paramater1', 'ura_paramater2', 'ura_paramater3', 'ura_paramater4', 'aoharu_paramater1',
#             'aoharu_paramater2', 'aoharu_paramater3', 'aoharu_paramater4', 'updateTime', 'addTime'
#         }

# 出退勤管理画面用
class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
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

