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
import copy

# 〓=================rwar=======
# pager
# https://blog.narito.ninja/detail/89
# 〓========================
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def paginate_queryset(request, queryset, count):
    """Pageオブジェクトを返す。
    ページングしたい場合に利用してください。
    countは、1ページに表示する件数です。
    返却するPgaeオブジェクトは、以下のような感じで使えます。
        {% if page_obj.has_previous %}
          <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
        {% endif %}
    また、page_obj.object_list で、count件数分の絞り込まれたquerysetが取得できます。
    """
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

# 〓========================
# うまツール関連
# 〓========================
from rest_framework import viewsets
from app_roster.models import umaCardUniqueBonus, umaCardMaster, umaCardSkillMaster, umaCardMessageMaster, umaWhiteFactor, umaWhiteFactor, umaMaster, SkillDetailMaster, SkillEvaluationMaster
# from app_roster.seliarizers import umaCardMasterSerializer
from pymongo import MongoClient
sys.path.append("app_roster/db/mongodb/config")
from setting_pymongo import settingPymongo
from pymongo import ASCENDING
from pymongo import DESCENDING

#////////////////
# サポートカードマスタ
#////////////////
def umaCardMasterLoad(request, typeno):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umacardmaster')
    f = mongo.find(filter={'cardTypeNo': typeno})
    # find = mongo.find(sort=[('cardMasterId', ASCENDING), ('cardName', ASCENDING)])
    count = f.count()

    for doc in f.sort([('cardMasterId', ASCENDING), ('cardName', ASCENDING)]):
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

# 指定のkeyの総数を取得する
def getValueCount(dimension, key, value):
    l = [d.get(key) for d in dimension]
    # count = 0
    # for d in dimension:
    #     if d[key] == value:
    #         count += 1
    return l.count(value)

# ////////////////
# サポートカードスキルマスタ
# ////////////////
def umaCardSkillMasterLoad(request, typeno):
    # paginate_by = 10
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umacardskillmaster')
    # find = mongo.find()
    # page = request.GET.get('page') # ページ数取得
    f = mongo.find(filter={'typeNo': typeno})
    # find = mongo.find(sort=[('carSkillMasterId', ASCENDING), ('typeName', ASCENDING)])
    findAnother = copy.deepcopy(f)
    count = f.count()
    cardIdCount = 0
    beforeCardId = 0

    for doc in f.sort([('carSkillMasterId', ASCENDING), ('typeName', ASCENDING)]):
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
        # query回数で落ちる
        if beforeCardId != doc['cardId']:
            findCopy = copy.deepcopy(findAnother)
            cardIdCount = getValueCount(findCopy, 'cardId', doc['cardId'])
            beforeCardId = doc['cardId']
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
             'cardIdCount': cardIdCount
             # 'cardIdCount': 1
             }
        )

    page_obj = paginate_queryset(request, returnMessageParams, 10)
    returnArray = {'cardSkillMaster': returnMessageParams, 'count': count, 'post_list': page_obj.object_list, 'page_obj': page_obj}
    # returnArray = {
    #     'post_list': page_obj.object_list,
    #     'page_obj': page_obj,
    # }
    # return render(request, 'app/post_list.html', context)
    return render(request, 'SearchCardSkillMasterView.html', returnArray)

    # post_list = Post.objects.all()
    # page_obj = paginate_queryset(request, post_list, 1)
    # context = {
    #     'post_list': page_obj.object_list,
    #     'page_obj': page_obj,
    # }
    # return render(request, 'app/post_list.html', context)

# ////////////////
# カードメッセージマスタ
# ////////////////
def umaCardMessageMasterLoad(request, typeno):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umacardmessagemaster')
    # find = mongo.find(filter={'cardMasterId': 1})
    if typeno == 99:
        f = mongo.find()
    else:
        f = mongo.find(filter={'cardTypeNo': typeno})

    # find = mongo.find(sort=[('cardId', ASCENDING),('messageId', ASCENDING)])
    findAnother = copy.deepcopy(f)
    count = f.count()
    cardIdCount = 0
    beforeCardId = 0

    for doc in f.sort([('cardid', ASCENDING), ('messageId', ASCENDING)]):
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
        doc.setdefault('cardIdCount', '')
        if beforeCardId != doc['cardid']:
            findCopy = copy.deepcopy(findAnother)
            cardIdCount = getValueCount(findCopy, 'cardid', doc['cardid'])
            beforeCardId = doc['cardid']
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
             'url': 'images/' + str(doc['cardid']) + '.png',
             'cardIdCount': cardIdCount
             }
        )
        returnArray = {'cardMessageMaster': returnMessageParams, 'count': count, 'displayFlag': typeno}
    return render(request, 'SearchCardMessageMasterView.html', returnArray)

#////////////////
# スキルマスタ
#////////////////
def umaSkillMasterLoad(request, typeno):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umaskillmaster')
    f = mongo.find(filter={'type': typeno})
    # find = mongo.find(sort=[('skillMasterId', ASCENDING), ('typeName', ASCENDING)])
    count = f.count()

    for doc  in f.sort([('id', ASCENDING), ('type', ASCENDING)]):
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
def umaCardUniqueBonusLoad(request, typeno):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umacarduniquebonus')
    f = mongo.find(filter={'typeNo': typeno})
    # find = mongo.find(sort=[('cardUniqueBonusId', ASCENDING), ('cardName', ASCENDING)])
    count = f.count()

    for doc in f.sort([('cardId', ASCENDING)]):
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
        doc.setdefault('url', '')
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
             'effect': doc['effect'],
             'url': 'images/' + str(doc['cardId']) + '.png'
             }
        )
        returnArray = {'cardUniqueBonusMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchUniqueBonusMasterView.html', returnArray)

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

# ////////////////
# ウママスタ
# ////////////////
def umaMasterLoad(request):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_umamaster')
    # find = mongo.find(filter={'cardMasterId': 1})
    find = mongo.find(sort=[('id', ASCENDING), ('rarity', ASCENDING)])
    count = find.count()

    for doc in find:
        # 空白対策
        doc.setdefault('id', '')
        doc.setdefault('rarity', '')
        doc.setdefault('umaName', '')
        doc.setdefault('turf', '')
        doc.setdefault('dirt', '')
        doc.setdefault('short', '')
        doc.setdefault('mile', '')
        doc.setdefault('mid', '')
        doc.setdefault('long', '')
        doc.setdefault('escape', '')
        doc.setdefault('preceding', '')
        doc.setdefault('insert', '')
        doc.setdefault('drivein', '')
        doc.setdefault('speed', '')
        doc.setdefault('stamina', '')
        doc.setdefault('power', '')
        doc.setdefault('guts', '')
        doc.setdefault('wise', '')
        doc.setdefault('star3uniqueSkill', '')
        doc.setdefault('uniqueSkill', '')
        doc.setdefault('defaultSkill1', '')
        doc.setdefault('defaultSkill2', '')
        doc.setdefault('defaultSkill3', '')
        doc.setdefault('awakeningLevel2', '')
        doc.setdefault('awakeningLevel3', '')
        doc.setdefault('awakeningLevel4', '')
        doc.setdefault('awakeningLevel5', '')
        doc.setdefault('nurturingSkill1', '')
        doc.setdefault('nurturingSkill2', '')
        doc.setdefault('nurturingSkill3', '')
        doc.setdefault('nurturingSkill4', '')
        doc.setdefault('nurturingSkill5', '')
        doc.setdefault('nurturingSkill6', '')
        doc.setdefault('nurturingSkill7', '')
        doc.setdefault('nurturingSkill8', '')
        doc.setdefault('nurturingSkill9', '')
        doc.setdefault('nurturingSkill10', '')
        doc.setdefault('nurturingSkill11', '')
        doc.setdefault('nurturingSkill12', '')

        # スキルマスタ配列格納
        returnMessageParams.append(
            {'id': doc['id'],
             'rarity': doc['rarity'],
             'umaName': doc['umaName'],
             'turf': doc['turf'],
             'dirt': doc['dirt'],
             'short': doc['short'],
             'mile': doc['mile'],
             'mid': doc['mid'],
             'long': doc['long'],
             'escape': doc['escape'],
             'preceding': doc['preceding'],
             'insert': doc['insert'],
             'drivein': doc['drivein'],
             'speed': doc['speed'],
             'stamina': doc['stamina'],
             'power': doc['power'],
             'guts': doc['guts'],
             'wise': doc['wise'],
             'star3uniqueSkill': doc['star3uniqueSkill'],
             'uniqueSkill': doc['uniqueSkill'],
             'defaultSkill1': doc['defaultSkill1'],
             'defaultSkill2': doc['defaultSkill2'],
             'defaultSkill3': doc['defaultSkill3'],
             'awakeningLevel2': doc['awakeningLevel2'],
             'awakeningLevel3': doc['awakeningLevel3'],
             'awakeningLevel4': doc['awakeningLevel4'],
             'awakeningLevel5': doc['awakeningLevel5'],
             'nurturingSkill1': doc['nurturingSkill1'],
             'nurturingSkill2': doc['nurturingSkill2'],
             'nurturingSkill3': doc['nurturingSkill3'],
             'nurturingSkill4': doc['nurturingSkill4'],
             'nurturingSkill5': doc['nurturingSkill5'],
             'nurturingSkill6': doc['nurturingSkill6'],
             'nurturingSkill7': doc['nurturingSkill7'],
             'nurturingSkill8': doc['nurturingSkill8'],
             'nurturingSkill9': doc['nurturingSkill9'],
             'nurturingSkill10': doc['nurturingSkill10'],
             'nurturingSkill11': doc['nurturingSkill11'],
             'nurturingSkill12': doc['nurturingSkill12']
             }
        )
        returnArray = {'umaMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchUmaMasterView.html', returnArray)

# ////////////////
# スキル詳細マスタ
# ////////////////
def umaSkillDetailMasterLoad(request, gereId, gere2Id):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_skilldetailmaster')
    # find = mongo.find(filter={'cardMasterId': 1})
    if gereId == 0 and gere2Id == 0:
        find = mongo.find(sort=[('id', ASCENDING)])
    else:
        find = mongo.find(filter={'gereId': gereId, 'genre2Id': gere2Id})

    # find = mongo.find(sort=[('id', ASCENDING)])
    count = find.count()

    for doc in find:
        # 空白対策
        doc.setdefault('id', '')
        doc.setdefault('genreName', '')
        doc.setdefault('gereId', '')
        doc.setdefault('genre2Name', '')
        doc.setdefault('genre2Id', '')
        doc.setdefault('branchNo', '')
        doc.setdefault('kindNo', '')
        doc.setdefault('skillName', '')
        doc.setdefault('explanation', '')
        doc.setdefault('category', '')
        doc.setdefault('rarity', '')
        doc.setdefault('activeCondition1', '')
        doc.setdefault('activeCondition2', '')
        doc.setdefault('activeCondition3', '')
        doc.setdefault('activeCondition4', '')
        doc.setdefault('activeCondition5', '')
        doc.setdefault('activeCondition6', '')
        doc.setdefault('activeCondition7', '')
        doc.setdefault('activeCondition8', '')
        doc.setdefault('activeCondition9', '')
        doc.setdefault('activeCondition10', '')
        doc.setdefault('effect1', '')
        doc.setdefault('effect2', '')
        doc.setdefault('effect3', '')
        doc.setdefault('effect4', '')
        doc.setdefault('effect5', '')
        doc.setdefault('effect6', '')
        doc.setdefault('effect7', '')
        doc.setdefault('effect8', '')
        doc.setdefault('effect9', '')
        doc.setdefault('effect10', '')
        doc.setdefault('wisepoint', '')
        doc.setdefault('getpoint', '')
        doc.setdefault('evaluationPoint', '')

        # スキルマスタ配列格納
        returnMessageParams.append(
            {'id': doc['id'],
             'genreName': doc['genreName'],
             'gereId': doc['gereId'],
             'genre2Name': doc['genre2Name'],
             'genre2Id': doc['genre2Id'],
             'branchNo': doc['branchNo'],
             'kindNo': doc['kindNo'],
             'skillName': doc['skillName'],
             'explanation': doc['explanation'],
             'category': doc['category'],
             'rarity': doc['rarity'],
             'activeCondition1': doc['activeCondition1'],
             'activeCondition2': doc['activeCondition2'],
             'activeCondition3': doc['activeCondition3'],
             'activeCondition4': doc['activeCondition4'],
             'activeCondition5': doc['activeCondition5'],
             'activeCondition6': doc['activeCondition6'],
             'activeCondition7': doc['activeCondition7'],
             'activeCondition8': doc['activeCondition8'],
             'activeCondition9': doc['activeCondition9'],
             'activeCondition10': doc['activeCondition10'],
             'effect1': doc['effect1'],
             'effect2': doc['effect2'],
             'effect3': doc['effect3'],
             'effect4': doc['effect4'],
             'effect5': doc['effect5'],
             'effect6': doc['effect6'],
             'effect7': doc['effect7'],
             'effect8': doc['effect8'],
             'effect9': doc['effect9'],
             'effect10': doc['effect10'],
             'wisepoint': doc['wisepoint'],
             'getpoint': doc['getpoint'],
             'evaluationPoint': doc['evaluationPoint']
             }
        )
        returnArray = {'umaCardSkillDetailMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchSkillDetailMasterView.html', returnArray)


# ////////////////
# スキル評価マスタ
# ////////////////
def umaSkillEvaluationMasterLoad(request, genreNo):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_skillevaluationmaster')
    # find = mongo.find(filter={'cardMasterId': 1})
    if genreNo == 99:
        find = mongo.find(sort=[('hurigana', ASCENDING)])
    elif genreNo == 0:
        find = mongo.find(sort=[('id', ASCENDING)])
    else:
        find = mongo.find(filter={'genreNo': genreNo})
    # find = mongo.find(sort=[('id', ASCENDING)])
    count = find.count()

    for doc in find:
        # 空白対策
        doc.setdefault('id', '')
        doc.setdefault('genreNo', '')
        doc.setdefault('genreName', '')
        doc.setdefault('skillName', '')
        doc.setdefault('champEvaluation', '')
        doc.setdefault('teamEvaluation', '')
        doc.setdefault('type', '')
        doc.setdefault('anotherSkill', '')
        doc.setdefault('effect', '')
        doc.setdefault('EvaluationSentence', '')
        doc.setdefault('needPint', '')
        doc.setdefault('evaluationPoint', '')
        doc.setdefault('evaluationEfficiency', '')
        doc.setdefault('hurigana', '')

        # スキルマスタ配列格納
        returnMessageParams.append(
            {'id': doc['id'],
             'genreNo': doc['genreNo'],
             'genreName': doc['genreName'],
             'skillName': doc['skillName'],
             'champEvaluation': doc['champEvaluation'],
             'teamEvaluation': doc['teamEvaluation'],
             'type': doc['type'],
             'anotherSkill': doc['anotherSkill'],
             'effect': doc['effect'],
             'EvaluationSentence': doc['EvaluationSentence'],
             'needPint': doc['needPint'],
             'evaluationPoint': doc['evaluationPoint'],
             'evaluationEfficiency': doc['evaluationEfficiency'],
             'hurigana': doc['hurigana']
             }
        )
        returnArray = {'umaSkillEvaluationMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchSkillEvaluationView.html', returnArray)

# ////////////////
# レースボーナスマスタ
# ////////////////
def umaRaceBonusMasterLoad(request, genreNo):
    returnArray = []
    returnMessageParams = []
    mongo = settingPymongo('rosterdb', 'app_roster_racebonumaster')
    # find = mongo.find(filter={'cardMasterId': 1})
    if genreNo == 99:
        find = mongo.find(sort=[('hurigana', ASCENDING)])
    elif genreNo == 0:
        find = mongo.find(sort=[('id', ASCENDING)])
    else:
        find = mongo.find(filter={'genreNo': genreNo})
    # find = mongo.find(sort=[('id', ASCENDING)])
    count = find.count()

    for doc in find:
        # 空白対策
        doc.setdefault('id', '')
        doc.setdefault('raceBonus', '')
        doc.setdefault('bonusName', '')
        doc.setdefault('contents', '')
        doc.setdefault('hurigana', '')

        # スキルマスタ配列格納
        returnMessageParams.append(
            {'id': doc['id'],
             'raceBonus': doc['raceBonus'],
             'bonusName': doc['bonusName'],
             'contents': doc['contents'],
             'hurigana': doc['hurigana']
             }
        )
        returnArray = {'umaRaceBonusMaster': returnMessageParams, 'count': count}
    return render(request, 'SearchRaceBonusMasterView.html', returnArray)

