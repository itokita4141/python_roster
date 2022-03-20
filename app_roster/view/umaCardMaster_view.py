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
sys.path.append("app_roster/db/sqlalchemy/migrate/config")
from setting_alchemy import Base
from setting_alchemy import ENGINE
from setting_alchemy import session
sys.path.append("app_roster/db/sqlalchemy/migrate/models")

# 〓========================
# うまツール関連
# 〓========================
from rest_framework import viewsets
from app_roster.models import umaCardUniqueBonus, umaCardMaster, umaCardSkillMaster, umaCardMessageMaster, umaWhiteFactor
# from app_roster.seliarizers import umaCardMasterSerializer
from pymongo import MongoClient
sys.path.append("app_roster/db/mongodb/config")
from setting_pymongo import settingPymongo
from pymongo import ASCENDING
from pymongo import DESCENDING

#////////////////
# サポートカードマスタ
#////////////////
def umaCardMasterLoad(request):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umacardmaster')
    # find = mongo.find(filter={'cardMasterId': 1})
    find = mongo.find(sort=[('cardMasterId', ASCENDING), ('cardName', ASCENDING)])
    count = find.count()

    for doc in find:
        # 空白対策
        doc.setdefault('id', '')
        doc.setdefault('cardMasterId', '')
        doc.setdefault('limitedOverNum', '')
        doc.setdefault('cardId', '')
        doc.setdefault('cardTypeNo', '')
        doc.setdefault('cardTypeName', '')
        doc.setdefault('cardName', '')
        doc.setdefault('rared', '')
        doc.setdefault('specialityRare', '')
        doc.setdefault('yarukiEffect', '')
        doc.setdefault('friendlyBonus', '')
        doc.setdefault('trainingEffect', '')
        doc.setdefault('speedBonus', '')
        doc.setdefault('staminaBonus', '')
        doc.setdefault('powerBonus', '')
        doc.setdefault('skillBonus', '')
        doc.setdefault('gutsBonus', '')
        doc.setdefault('wiseBonus', '')
        doc.setdefault('wiseBonus100', '')
        doc.setdefault('hintLevel', '')
        doc.setdefault('hintIncidence', '')
        doc.setdefault('defaultKizunaGage', '')
        doc.setdefault('defaultSpeed', '')
        doc.setdefault('defaultStamina', '')
        doc.setdefault('defaultPower', '')
        doc.setdefault('defaultWise', '')
        doc.setdefault('defaultGuts', '')
        doc.setdefault('raceBonus', '')
        doc.setdefault('fanNumber_Bonus', '')
        doc.setdefault('eventEffect', '')
        doc.setdefault('wiseFriendlyRecoverlyAmount', '')
        doc.setdefault('eventRecoveryAmont', '')
        doc.setdefault('lifeComsumptionDown', '')
        doc.setdefault('failureRateDown', '')
        doc.setdefault('ura_paramater1', '')
        doc.setdefault('ura_paramater2', '')
        doc.setdefault('ura_paramater3', '')
        doc.setdefault('ura_paramater4', '')
        doc.setdefault('aoharu_paramater1', '')
        doc.setdefault('aoharu_paramater2', '')
        doc.setdefault('aoharu_paramater3', '')
        doc.setdefault('aoharu_paramater4', '')
        doc.setdefault('updateTime', '')
        doc.setdefault('addTime', '')
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
             'fanNumber': doc['fanNumber Bonus'],
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
             'url': 'images/' + str(doc['cardId']) + '.png',
             'updateTime': doc['updateTime'],
             'addTime': doc['addTime']
             }
        )
        returnArray = {'cardMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchCardMasterView.html', returnArray)

# ////////////////
# サポートカードスキルマスタ
# ////////////////
def umaCardSkillMasterLoad(request):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umacardskillmaster')
    # find = mongo.find(filter={'cardMasterId': 1})
    find = mongo.find(sort=[('carSkillMasterId', ASCENDING), ('typeName', ASCENDING)])
    count = find.count()

    for doc in find:
        # findCardId = mongo.find(filter={'cardId': doc['cardId']})
        # cardIdCount = findCardId.count()
        # 空白対策
        doc.setdefault('id', '')
        doc.setdefault('carSkillMasterId', '')
        doc.setdefault('typeNo', '')
        doc.setdefault('typeName', '')
        doc.setdefault('cardId', '')
        doc.setdefault('cardName', '')
        doc.setdefault('sortNum', '')
        doc.setdefault('eventType', '')
        doc.setdefault('eventTypeName', '')
        doc.setdefault('skillName', '')
        doc.setdefault('skillContents', '')
        doc.setdefault('cardIdCount', '')

        # スキルマスタ配列格納
        returnMessageParams.append(
            {'id': doc['id'],
             'carSkillMasterId': doc['carSkillMasterId'],
             'typeNo': doc['typeNo'],
             'typeName': doc['typeName'],
             'cardId': doc['cardId'],
             'cardName': doc['cardName'],
             'sortNum': doc['sortNum'],
             'eventType': doc['eventType'],
             'eventTypeName': doc['eventTypeName'],
             'skillName': doc['skillName'],
             'skillContents': doc['skillContents'],
             'url': 'images/' + str(doc['cardId']) + '.png',
             # 'cardIdCount': cardIdCount
             'cardIdCount': 1
             }
        )
        returnArray = {'cardSkillMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchCardSkillMasterView.html', returnArray)

#////////////////
# スキルマスタ
#////////////////
def umaSkillMasterLoad(request):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umaskillmaster')
    # find = mongo.find(filter={'cardMasterId': 1})
    find = mongo.find(sort=[('skillMasterId', ASCENDING), ('typeName', ASCENDING)])
    count = find.count()

    for doc in find:
        # 空白対策
        doc.setdefault('id', '')
        doc.setdefault('skillMasterId', '')
        doc.setdefault('type', '')
        doc.setdefault('typeName', '')
        doc.setdefault('type2', '')
        doc.setdefault('skillName', '')
        doc.setdefault('skillContents', '')
        doc.setdefault('skillType', '')
        doc.setdefault('raceEvaluation', '')
        doc.setdefault('champEvaluation', '')
        doc.setdefault('possetionSupportCards', '')
        doc.setdefault('possetionsCharactors', '')
        # スキルマスタ配列格納
        returnMessageParams.append(
            {'id': doc['id'],
             'skillMasterId': doc['skillMasterId'],
             'type': doc['type'],
             'typeName': doc['typeName'],
             'type2': doc['type2'],
             'skillName': doc['skillName'],
             'skillContents': doc['skillContents'],
             'skillType': doc['skillType'],
             'raceEvaluation': doc['raceEvaluation'],
             'champEvaluation': doc['champEvaluation'],
             'possetionSupportCards': doc['possetionSupportCards'],
             'possetionsCharactors': doc['possetionsCharactors']
             }
        )
        returnArray = {'skillMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchSkillMasterView.html', returnArray)

# ////////////////
# 固有ボーナスマスタ
# ////////////////
def umaCardUniqueBonusLoad(request):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umacarduniquebonus')
    # find = mongo.find(filter={'cardMasterId': 1})
    find = mongo.find(sort=[('cardUniqueBonusId', ASCENDING), ('cardName', ASCENDING)])
    count = find.count()

    for doc in find:
        # 空白対策
        doc.setdefault('id', '')
        doc.setdefault('cardUniqueBonusId', '')
        doc.setdefault('typeNo', '')
        doc.setdefault('typeName', '')
        doc.setdefault('cardId', '')
        doc.setdefault('cardName', '')
        doc.setdefault('aoharuEvaluationLimit0', '')
        doc.setdefault('aoharuEvaluationLimit4', '')
        doc.setdefault('uraFinalsLimit0', '')
        doc.setdefault('uraFinalsLimit4', '')
        doc.setdefault('lisetMarathonRank', '')
        doc.setdefault('rank', '')
        doc.setdefault('referenceInformation', '')
        doc.setdefault('uniqueFactorName', '')
        doc.setdefault('getLevel', '')
        doc.setdefault('effect', '')
        # スキルマスタ配列格納
        returnMessageParams.append(
            {'id': doc['id'],
             'cardUniqueBonusId': doc['cardUniqueBonusId'],
             'typeNo': doc['typeNo'],
             'typeName': doc['typeName'],
             'cardId': doc['cardId'],
             'cardName': doc['cardName'],
             'aoharuEvaluationLimit0': doc['aoharuEvaluationLimit0'],
             'aoharuEvaluationLimit4': doc['aoharuEvaluationLimit4'],
             'uraFinalsLimit0': doc['uraFinalsLimit0'],
             'uraFinalsLimit4': doc['uraFinalsLimit4'],
             'lisetMarathonRank': doc['lisetMarathonRank'],
             'rank': doc['rank'],
             'referenceInformation': doc['referenceInformation'],
             'uniqueFactorName': doc['uniqueFactorName'],
             'getLevel': doc['getLevel'],
             'effect': doc['effect']
             }
        )
        returnArray = {'cardUniqueBonusMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchUniqueBonusMasterView.html', returnArray)

# ////////////////
# カードメッセージマスタ
# ////////////////
def umaCardMessageMasterLoad(request):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umacardmessagemaster')
    # find = mongo.find(filter={'cardMasterId': 1})
    find = mongo.find(sort=[('carSkillMasterId', ASCENDING), ('typeName', ASCENDING)])
    count = find.count()

    for doc in find:
        # 空白対策
        doc.setdefault('id', '')
        doc.setdefault('cardMessageMasterId', '')
        doc.setdefault('cardTypeNo', '')
        doc.setdefault('cardTypeName', '')
        doc.setdefault('cardid', '')
        doc.setdefault('cardName', '')
        doc.setdefault('type', '')
        doc.setdefault('messageId', '')
        doc.setdefault('messageEventId', '')
        doc.setdefault('eventTypeId', '')
        doc.setdefault('eventType', '')
        doc.setdefault('title', '')
        doc.setdefault('selectType', '')
        doc.setdefault('result', '')
        doc.setdefault('result1', '')
        doc.setdefault('result2', '')
        doc.setdefault('result3', '')
        doc.setdefault('result4', '')
        doc.setdefault('result5', '')
        doc.setdefault('result6', '')
        doc.setdefault('result7', '')
        doc.setdefault('result8', '')
        doc.setdefault('result9', '')
        doc.setdefault('result10', '')
        # スキルマスタ配列格納
        returnMessageParams.append(
            {'id': doc['id'],
             'cardMessageMasterId': doc['cardMessageMasterId'],
             'cardTypeNo': doc['cardTypeNo'],
             'cardTypeName': doc['cardTypeName'],
             'cardid': doc['cardid'],
             'cardName': doc['cardName'],
             'type': doc['type'],
             'messageId': doc['messageId'],
             'messageEventId': doc['messageEventId'],
             'eventTypeId': doc['eventTypeId'],
             'eventType': doc['eventType'],
             'title': doc['title'],
             'selectType': doc['selectType'],
             'result': doc['result'],
             'result1': doc['result1'],
             'result2': doc['result2'],
             'result3': doc['result3'],
             'result4': doc['result4'],
             'result5': doc['result5'],
             'result6': doc['result6'],
             'result7': doc['result7'],
             'result8': doc['result8'],
             'result9': doc['result9'],
             'result10': doc['result10'],
             }
        )
        returnArray = {'cardMessageMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchCardMessageMasterView.html', returnArray)

# ////////////////
# 白因子マスタ
# ////////////////
def umaWhiteFactorLoad(request):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umawhitefactor')
    # find = mongo.find(filter={'cardMasterId': 1})
    find = mongo.find(sort=[('whiteFactorId', ASCENDING), ('factorName', ASCENDING)])
    count = find.count()

    for doc in find:
        # 空白対策
        doc.setdefault('id', '')
        doc.setdefault('whiteFactorId', '')
        doc.setdefault('factorName', '')
        doc.setdefault('raceTiming', '')
        doc.setdefault('raceInfo', '')
        doc.setdefault('factor1', '')
        doc.setdefault('factor2', '')
        doc.setdefault('factor3', '')

        # スキルマスタ配列格納
        returnMessageParams.append(
            {'id': doc['id'],
             'whiteFactorId': doc['whiteFactorId'],
             'factorName': doc['factorName'],
             'raceTiming': doc['raceTiming'],
             'raceInfo': doc['raceInfo'],
             'factor1': doc['factor1'],
             'factor2': doc['factor2'],
             'factor3': doc['factor3']
             }
        )
        returnArray = {'whiteFactorMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchWhiteFactorView.html', returnArray)







