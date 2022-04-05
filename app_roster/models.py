# from django.db import models
from djongo import models


class Users(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),
    userId = models.CharField(primary_key=True, max_length=10),
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

class Attendances(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),
    attendanceId = models.CharField(primary_key=True, max_length=10),
    userId = models.CharField(max_length=10),
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

class Logs(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),
    logId = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='LOG_ID'),
    userId = models.CharField(primary_key=True,max_length=10),
    content = models.TextField(null=True,blank=True,max_length=1000),
    deleteFlag = models.BooleanField(default=False),
    updateTime = models.DateField(null=False),
    addTime = models.BooleanField(null=True),

    def __str__(self):
        return str(self.__dict__)

###########
# ウマ娘用
###########
# 固有ボーナスマスタ
class umaCardUniqueBonus(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),  # ID
    cardUniqueBonusId = models.CharField(auto_created=False, primary_key=False, serialize=False, verbose_name='CARDUNIQUEBONUSID'),  # cardUniqueBonusId
    typeNo = models.SmallIntegerField(null=False),                         # タイプ番号
    typeName = models.CharField(max_length=100,null=False),                # タイプ名称
    cardId = models.SmallIntegerField(null=False),                         # カードID
    cardName = models.CharField(max_length=100,null=False),                # カード名称
    aoharuEvaluationLimit0 = models.CharField(max_length=100,null=False),  # "アオハル評価 無凸"
    aoharuEvaluationLimit4 = models.CharField(max_length=100,null=False),  # "アオハル評価 完凸"
    uraFinalsLimit0 = models.CharField(max_length=100,null=False),         # "URAファイナルズ 無凸"
    uraFinalsLimit4 = models.CharField(max_length=100,null=False),         # "URAファイナルズ 完凸"
    lisetMarathonRank = models.CharField(max_length=100,null=False),       # リセマラ
    rank = models.CharField(max_length=100,null=False),                    # ランク
    referenceInformation = models.CharField(max_length=100,null=False),    # 参考情報
    uniqueFactorName = models.CharField(max_length=100,null=False),        # 固有スキル名称
    getLevel = models.CharField(max_length=100,null=False),                # レベル
    effect = models.CharField(max_length=100,null=False),                  # 効果
    updateTime = models.DateField(null=False),                             # 更新時間
    addTime = models.BooleanField(null=True),                              # 追加時間

    def __str__(self):
        return str(self.__dict__)

# 固有スキルマスタ
class umaSkillMaster(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),
    skillMasterId = models.BigIntegerField(null=False,primary_key=False),  # id
    typeNo = models.SmallIntegerField(null=False),                         # タイプ番号
    typeName = models.CharField(max_length=10,null=False),                 # タイプ名称
    type2 = models.CharField(max_length=10,null=False),                    # 総合評価ランク
    skillName = models.CharField(max_length=20,null=False),                # スキル名
    skillContents = models.CharField(max_length=1000,null=False),          # スキル内容
    skillType = models.CharField(max_length=10,null=False),                # 作戦
    raceEvaluation = models.CharField(max_length=1),                       # 評価競技場
    champEvaluation = models.CharField(max_length=5),                      # 評価チャンミ
    possetionSupportCards = models.CharField(max_length=1000),             # 所持サポートカード
    possetionCharactors = models.CharField(max_length=1000),               # 所持キャラ
    updateTime = models.DateField(null=False),                             # 更新時間
    addTime = models.BooleanField(null=True),                              # 追加時間

    def __str__(self):
        return str(self.__dict__)

# カードマスタ
class umaCardMaster(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),
    cardMasterId = models.BigIntegerField(null=False,primary_key=False),  # ID
    limitedOverNum = models.SmallIntegerField(null=False),                # 凸数
    cardId = models.IntegerField(null=False),                             # カードID
    cardTypeNo = models.SmallIntegerField(null=False),                    # カードタイプ
    cardTypeName = models.CharField(null=False,max_length=10),            # カードタイプ名称
    cardName = models.CharField(null=False,max_length=100),               # カード名称
    rared = models.SmallIntegerField(null=False),                         # レア度
    specialityRare = models.CharField(max_length=10),                     # 得意率
    yarukiEffect = models.CharField(max_length=10),                       # やる気効果
    friendlyBonus = models.CharField(max_length=10),                      # 友情ボーナス
    trainingEffect = models.CharField(max_length=10),                     # トレーニング効果
    speedBonus = models.CharField(max_length=10),                         # スピードボーナス
    staminaBonus = models.CharField(max_length=10),                       # パワーボーナス
    powerBonus = models.CharField(max_length=10),                         # スキルPtボーナス
    skillBonus = models.CharField(max_length=10),                           # ヒントLv
    gutsBonus = models.CharField(max_length=10),                          # ヒント発生率
    wiseBonus = models.CharField(max_length=10),                          # 初期絆ゲージ
    wiseBonus100 = models.CharField(max_length=10),                       # 初期スピード
    hintLevel = models.CharField(max_length=10),                          # 初期スタミナ
    hintIncidence = models.CharField(max_length=10),                      # 初期パワー
    defaultKizunaGage = models.CharField(max_length=10),                  # 初期賢さ
    defaultSpeed = models.CharField(max_length=10),                       # 初期根性
    defaultStamina = models.CharField(max_length=10),                     # レースボーナス
    defaultPower = models.CharField(max_length=10),                       # ファン数ボーナス
    defaultWise = models.CharField(max_length=10),                        # トレーニング効果
    defaultGuts = models.CharField(max_length=10),                        # イベント効果
    raceBonus = models.CharField(max_length=10),                          # 賢さ友情回復量
    fanNumber_Bonus = models.CharField(max_length=10),                    # イベント回復量
    eventEffect = models.CharField(max_length=10),                        # 失敗率ダウン
    wiseFriendlyRecoverlyAmount = models.CharField(max_length=10),        # スタミナボーナス
    eventRecoveryAmont = models.CharField(max_length=10),                 # 根性ボーナス
    lifeComsumptionDown = models.CharField(max_length=10),                # 賢さボーナス
    failureRateDown = models.CharField(max_length=10),                    # 賢さボーナス絆100
    ura_paramater1 = models.CharField(max_length=10),                     # URA上昇値(単/Lv5/友情/好)1
    ura_paramater2 = models.CharField(max_length=10),                     # URA上昇値(単/Lv5/友情/好)2
    ura_paramater3 = models.CharField(max_length=10),                     # URA上昇値(単/Lv5/友情/好)3
    ura_paramater4 = models.CharField(max_length=10),                     # URA上昇値(単/Lv5/友情/好)4
    aoharu_paramater1 = models.CharField(max_length=10),                  # アオハル上昇値(単/Lv5/友情/絶好)1
    aoharu_paramater2 = models.CharField(max_length=10),                  # アオハル上昇値(単/Lv5/友情/絶好)2
    aoharu_paramater3 = models.CharField(max_length=10),                  # アオハル上昇値(単/Lv5/友情/絶好)3
    aoharu_paramater4 = models.CharField(max_length=10),                  # アオハル上昇値(単/Lv5/友情/絶好)4
    updateTime = models.DateField(null=False),                            # 更新時間
    addTime = models.BooleanField(null=True),                             # 追加時間

    def __str__(self):
        return str(self.__dict__)

# カードスキルマスタ
class umaCardSkillMaster(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),
    cardSkillMasterId = models.BigIntegerField(null=False, primary_key=False),  # ID
    typeNo = models.SmallIntegerField(null=False),                              # タイプ番号
    typeName = models.CharField(max_length=100, null=False),                    # タイプ名称
    cardId = models.SmallIntegerField(null=False),                              # カードID
    cardName = models.CharField(max_length=100, null=False),                    # カード名称
    sortNum = models.CharField(max_length=100, null=False),                     # ソート順
    eventType = models.SmallIntegerField( null=False),                          # イベントタイプ
    eventTypeName = models.CharField(max_length=100, null=False),               # イベントタイプ名称
    skillName = models.CharField(max_length=100, null=False),                   # スキル名称
    skillContents = models.CharField(max_length=100, null=False),               # スキル内容
    updateTime = models.DateField(null=False),                                  # 更新時間
    addTime = models.BooleanField(null=True),                                   # 追加時間

    def __str__(self):
        return str(self.__dict__)

class umaCardMessageMaster(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),
    cardMessageMasterId = models.BigIntegerField(null=True,primary_key=False),  # ID
    cardTypeNo = models.SmallIntegerField( null=True),                          # カード種別番号
    cardTypeName = models.CharField(max_length=100, null=True),                 # カード種別名称
    cardMessageMasterId = models.SmallIntegerField(null=True),                  # カードID
    cardName = models.CharField(max_length=100, null=True),                     # カード名称
    type = models.SmallIntegerField(null=True),                                 # タイプNO
    messageId = models.SmallIntegerField(null=True),                            # メッセージID
    messageEventId = models.SmallIntegerField(null=True),                       # メッセージイベントID
    eventTypeId = models.SmallIntegerField(null=True),                          # イベントタイプID
    eventType = models.CharField(max_length=100, null=True),                    # イベントタイプ
    title = models.CharField(max_length=100, null=True),                        # タイトル
    selectType = models.CharField(max_length=100, null=True),                   # 選択肢タイプ
    result = models.CharField(max_length=100, null=True),                       # 結果
    result1 = models.CharField(max_length=100, null=True),                      # 結果1
    result2 = models.CharField(max_length=100, null=True),                      # 結果2
    result3 = models.CharField(max_length=100, null=True),                      # 結果3
    result4 = models.CharField(max_length=100, null=True),                      # 結果4
    result5 = models.CharField(max_length=100, null=True),                      # 結果5
    result6 = models.CharField(max_length=100, null=True),                      # 結果6
    result7 = models.CharField(max_length=100, null=True),                      # 結果7
    result8 = models.CharField(max_length=100, null=True),                      # 結果8
    result9 = models.CharField(max_length=100, null=True),                      # 結果9
    result10 = models.CharField(max_length=100, null=True),                     # 結果10
    updateTime = models.DateField(null=True),                                   # 更新時間
    addTime = models.BooleanField(null=True),                                    # 追加時間

    def __str__(self):
        return str(self.__dict__)

# 白マスタ因子マスタ
class umaWhiteFactor(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),
    whiteFactorId = models.CharField(max_length=100, null=False,primary_key=False),  # ID
    factorName = models.CharField(max_length=100, null=False),                       # レース＝因子名
    raceTiming = models.CharField(max_length=100, null=False),                       # レース情報
    raceInfo = models.CharField(max_length=100, null=False),                         # レース情報
    factor1 = models.CharField(max_length=100, null=False),                          # 継承効果1
    factor2 = models.CharField(max_length=100, null=False),                          # 継承効果2
    factor3 = models.CharField(max_length=100, null=False),                          # 継承効果3
    updateTime = models.DateField(null=False),                                       # 更新時間
    addTime = models.BooleanField(null=True),                                        # 追加時間

    def __str__(self):
        return str(self.__dict__)

# 育成うまマスタ
class umaMaster(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),    # ID
    rarity = models.CharField(max_length=100, null=False,primary_key=False),                                # 星
    umaName = models.CharField(max_length=100, null=False,primary_key=False),                               # 名前
    turf = models.CharField(max_length=100, null=False,primary_key=False),                                  # バ適正
    dirt = models.CharField(max_length=100, null=False,primary_key=False),                                  # ダート補正
    short = models.CharField(max_length=100, null=False,primary_key=False),                                 # 距離適正
    mile = models.CharField(max_length=100, null=False,primary_key=False),                                  # マイル適正
    mid = models.CharField(max_length=100, null=False,primary_key=False),                                   # 中距離適正
    long = models.CharField(max_length=100, null=False,primary_key=False),                                  # 長距離適正
    escape = models.CharField(max_length=100, null=False,primary_key=False),                                # 逃げて規制
    preceding = models.CharField(max_length=100, null=False,primary_key=False),                             # 先行適正
    insert = models.CharField(max_length=100, null=False,primary_key=False),                                # 差し適正
    drivein = models.CharField(max_length=100, null=False,primary_key=False),                               # 追込適正
    speed = models.CharField(max_length=100, null=False,primary_key=False),                                 # 成長スピード
    stamina = models.CharField(max_length=100, null=False,primary_key=False),                               # 成長スタミナ
    power = models.CharField(max_length=100, null=False,primary_key=False),                                 # 成長パワー
    guts = models.CharField(max_length=100, null=False,primary_key=False),                                  # 成長根性
    wise = models.CharField(max_length=100, null=False,primary_key=False),                                  # 成長賢さ
    star3uniqueSkill = models.CharField(max_length=100, null=False,primary_key=False),                      # ★3固有
    uniqueSkill = models.CharField(max_length=100, null=False,primary_key=False),                           # 固有
    defaultSkill1 = models.CharField(max_length=100, null=False,primary_key=False),                         # 初期
    defaultSkill2 = models.CharField(max_length=100, null=False,primary_key=False),                         # 初期
    defaultSkill3 = models.CharField(max_length=100, null=False,primary_key=False),                         # 初期
    awakeningLevel2 = models.CharField(max_length=100, null=False,primary_key=False),                       # 覚醒Lv2
    awakeningLevel3 = models.CharField(max_length=100, null=False,primary_key=False),                       # 覚醒Lv3
    awakeningLevel4 = models.CharField(max_length=100, null=False,primary_key=False),                       # 覚醒Lv4
    awakeningLevel5 = models.CharField(max_length=100, null=False,primary_key=False),                       # 覚醒Lv5
    nurturingSkill1 = models.CharField(max_length=100, null=False,primary_key=False),                       # 育成1
    nurturingSkill2 = models.CharField(max_length=100, null=False,primary_key=False),                       # 育成2
    nurturingSkill3 = models.CharField(max_length=100, null=False,primary_key=False),                       # 育成3
    nurturingSkill4 = models.CharField(max_length=100, null=False,primary_key=False),                       # 育成4
    nurturingSkill5 = models.CharField(max_length=100, null=False,primary_key=False),                       # 育成5
    nurturingSkill6 = models.CharField(max_length=100, null=False,primary_key=False),                       # 育成6
    nurturingSkill7 = models.CharField(max_length=100, null=False,primary_key=False),                       # 育成7
    nurturingSkill8 = models.CharField(max_length=100, null=False,primary_key=False),                       # 育成8
    nurturingSkill9 = models.CharField(max_length=100, null=False,primary_key=False),                       # 育成9
    nurturingSkill10 = models.CharField(max_length=100, null=False,primary_key=False),                      # 育成10
    nurturingSkill11 = models.CharField(max_length=100, null=False,primary_key=False),                      # 育成11
    nurturingSkill12 = models.CharField(max_length=100, null=False,primary_key=False),                      # 育成12
    updateTime = models.DateField(null=False),                                                              # 更新時間
    addTime = models.BooleanField(null=True),                                                               # 追加時間

    def __str__(self):
        return str(self.__dict__)

# スキル詳細マスタ
class SkillDetailMaster(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=False, serialize=False, verbose_name='ID'),  # id
    genreName = models.CharField(max_length=100, null=False,primary_key=False),   # ジャンル１
    gereId = models.CharField(max_length=100, null=False,primary_key=False),   # ジャンル1id
    genre2Name = models.CharField(max_length=100, null=False,primary_key=False),   # ジャンル２
    genre2Id = models.CharField(max_length=100, null=False,primary_key=False),   # ジャンル2id
    branchNo = models.CharField(max_length=100, null=False,primary_key=False),   # 枝番
    kindNo = models.CharField(max_length=100, null=False,primary_key=False),   # 種類
    skillName = models.CharField(max_length=100, null=False,primary_key=False),   # スキル名
    explanation = models.CharField(max_length=100, null=False,primary_key=False),   # 説明文
    category = models.CharField(max_length=100, null=False,primary_key=False),   # カテゴリ
    rarity = models.CharField(max_length=100, null=False,primary_key=False),   # レアリティ
    activeCondition1 = models.CharField(max_length=100, null=False,primary_key=False),   # 条件１
    activeCondition2 = models.CharField(max_length=100, null=False,primary_key=False),   # 条件２
    activeCondition3 = models.CharField(max_length=100, null=False,primary_key=False),   # 条件３
    activeCondition4 = models.CharField(max_length=100, null=False,primary_key=False),   # 条件４
    activeCondition5 = models.CharField(max_length=100, null=False,primary_key=False),   # 条件５
    activeCondition6 = models.CharField(max_length=100, null=False,primary_key=False),   # 条件６
    activeCondition7 = models.CharField(max_length=100, null=False,primary_key=False),   # 条件７
    activeCondition8 = models.CharField(max_length=100, null=False,primary_key=False),   # 条件８
    activeCondition9 = models.CharField(max_length=100, null=False,primary_key=False),   # 条件９
    activeCondition10 = models.CharField(max_length=100, null=False,primary_key=False),   # 条件１０
    effect1 = models.CharField(max_length=100, null=False,primary_key=False),   # 効果量１
    effect2 = models.CharField(max_length=100, null=False,primary_key=False),   # 効果量２
    effect3 = models.CharField(max_length=100, null=False,primary_key=False),   # 効果量３
    effect4 = models.CharField(max_length=100, null=False,primary_key=False),   # 効果量４
    effect5 = models.CharField(max_length=100, null=False,primary_key=False),   # 効果量５
    effect6 = models.CharField(max_length=100, null=False,primary_key=False),   # 効果量６
    effect7 = models.CharField(max_length=100, null=False,primary_key=False),   # 効果量７
    effect8 = models.CharField(max_length=100, null=False,primary_key=False),   # 効果量８
    effect9 = models.CharField(max_length=100, null=False,primary_key=False),   # 効果量9
    effect10 = models.CharField(max_length=100, null=False,primary_key=False),   # 効果量10
    wisepoint = models.CharField(max_length=100, null=False,primary_key=False),   # 賢さ判定
    getpoint = models.CharField(max_length=100, null=False,primary_key=False),   # 取得ポイント
    evaluationPoint = models.CharField(max_length=100, null=False,primary_key=False),   # 評価点
    updateTime = models.DateField(null=False),                                              # 更新時間
    addTime = models.BooleanField(null=True),                                               # 追加時間

    def __str__(self):
        return str(self.__dict__)

# スキル評価マスタ
class SkillEvaluationMaster(models.Model):
    id = models.CharField(max_length=100, null=False,primary_key=False),   # ID
    genreNo = models.CharField(max_length=100, null=False,primary_key=False),   # ジャンル番号
    genreName = models.CharField(max_length=100, null=False,primary_key=False),   # 種類
    skillName = models.CharField(max_length=100, null=False,primary_key=False),   # スキル
    champEvaluation = models.CharField(max_length=100, null=False,primary_key=False),   # チャンミ評価
    teamEvaluation = models.CharField(max_length=100, null=False,primary_key=False),   # 競技場評価
    type = models.CharField(max_length=100, null=False,primary_key=False),   # 種類
    anotherSkill = models.CharField(max_length=100, null=False,primary_key=False),   # 上位スキル
    effect = models.CharField(max_length=100, null=False,primary_key=False),   # 効果
    EvaluationSentence = models.CharField(max_length=100, null=False,primary_key=False),   # 評価文
    needPint = models.CharField(max_length=100, null=False,primary_key=False),   # 必要Pt
    evaluationPoint = models.CharField(max_length=100, null=False,primary_key=False),   # 評価点
    evaluationEfficiency = models.CharField(max_length=100, null=False,primary_key=False),   # 評価効率
    updateTime = models.DateField(null=False),                                              # 更新時間
    addTime = models.BooleanField(null=True),                                               # 追加時間

    def __str__(self):
        return str(self.__dict__)


