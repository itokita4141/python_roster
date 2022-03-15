import sys
import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import TemplateView  # テンプレートタグ
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from .models import Users, Attendances
sys.path.append("app_roster/db/sqlalchemy/migrate/config")
from setting_alchemy import Base
from setting_alchemy import ENGINE
from setting_alchemy import session
sys.path.append("app_roster/db/sqlalchemy/migrate/models")

# 〓========================
# うまツール関連
# 〓========================
from rest_framework import viewsets
from app_roster.models import umaCardMaster, umaCardSkillMaster, umaCardMessageMaster, umaWhiteFactor
# from app_roster.seliarizers import umaCardMasterSerializer
from pymongo import MongoClient
sys.path.append("app_roster/db/mongodb/config")
from setting_pymongo import settingPymongo
from pymongo import ASCENDING
from pymongo import DESCENDING

def umaCardMasterLoad(request):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umacardmaster')
    # find = mongo.find(filter={'cardMasterId': 1})
    find = mongo.find(sort=[('cardMasterId', ASCENDING), ('cardName', ASCENDING)])
    count = find.count()

    for doc in find:
        returnMessageParams.append(
            {'id': doc['id'],
             'cardMasterId': doc['cardMasterId'],
             'limitedOverNum': doc['limitedOverNum'],
             'cardId': doc['cardId'],
             'cardTypeNo': doc['cardTypeNo'],
             'cardTypeName': doc['cardTypeName'],
             'cardName': doc['cardName'],
             'rared': doc['rared'],
             'specialityRare': doc['specialityRare'],
             'yarukiEffect': doc['yarukiEffect'],
             'friendlyBonus': doc['friendlyBonus'],
             'trainingEffect': doc['trainingEffect'],
             'speedBonus': doc['speedBonus'],
             'staminaBonus': doc['staminaBonus'],
             'powerBonus': doc['powerBonus'],
             'skillBonus': doc['skillBonus'],
             'gutsBonus': doc['gutsBonus'],
             'wiseBonus': doc['wiseBonus'],
             'wiseBonus100': doc['wiseBonus100'],
             'hintLevel': doc['hintLevel'],
             'hintIncidence': doc['hintIncidence'],
             'defaultKizunaGage': doc['defaultKizunaGage'],
             'defaultSpeed': doc['defaultSpeed'],
             'defaultStamina': doc['defaultStamina'],
             'defaultPower': doc['defaultPower'],
             'defaultWise': doc['defaultWise'],
             'defaultGuts': doc['defaultGuts'],
             'raceBonus': doc['raceBonus'],
             'fanNumber_Bonus': doc['fanNumber_Bonus'],
             # 'trainingEffect': doc['trainingEffect'],
             'eventEffect': doc['eventEffect'],
             'wiseFriendlyRecoverlyAmount': doc['wiseFriendlyRecoverlyAmount'],
             'eventRecoveryAmont': doc['eventRecoveryAmont'],
             'lifeComsumptionDown': doc['lifeComsumptionDown'],
             'failureRateDown': doc['failureRateDown'],
             'ura_paramater1': doc['ura_paramater1'],
             'ura_paramater2': doc['ura_paramater2'],
             'ura_paramater3': doc['ura_paramater3'],
             'ura_paramater4': doc['ura_paramater4'],
             'aoharu_paramater1': doc['aoharu_paramater1'],
             'aoharu_paramater2': doc['aoharu_paramater2'],
             'aoharu_paramater3': doc['aoharu_paramater3'],
             'aoharu_paramater4': doc['aoharu_paramater4'],
             'updateTime': doc['updateTime'],
             'addTime': doc['addTime']
             }
        )
        # id
        # cardMasterId
        # limitedOverNum
        # cardId
        # cardTypeNo
        # cardTypeName
        # cardName
        # rared
        # specialityRare
        # yarukiEffect
        # friendlyBonus
        # trainingEffect
        # speedBonus
        # staminaBonus
        # powerBonus
        # skillBonus
        # gutsBonus
        # wiseBonus
        # wiseBonus100
        # hintLevel
        # hintIncidence
        # defaultKizunaGage
        # defaultSpeed
        # defaultStamina
        # defaultPower
        # defaultWise
        # defaultGuts
        # raceBonus
        # fanNumber_Bonus
        # trainingEffect
        # eventEffect
        # wiseFriendlyRecoverlyAmount
        # eventRecoveryAmont
        # lifeComsumptionDown
        # failureRateDown
        # ura_paramater1
        # ura_paramater2
        # ura_paramater3
        # ura_paramater4
        # aoharu_paramater1
        # aoharu_paramater2
        # aoharu_paramater3
        # aoharu_paramater4
        # updateTime
        # addTime
        print(doc['cardMasterId'])
        print(doc['cardName'])

        returnArray = {'cardMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchCardMasterView.html', returnArray)





