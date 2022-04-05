from django.contrib import admin
from django.urls import include, path
import sys
sys.path.append("view/")
from .views import *
from .view.login_view import *
from .view.login_list import *
from rest_framework import routers
from app_roster import views
from .view.umaCardMaster_view import *

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet)
router.register(r'attendances', views.AttendancesViewSet)
router.register(r'logs', views.LogsViewSet)
# router.register('umaCardUniqueBonus', views.umaCardUniqueBonusViewSet)
# router.register('umaSkillMaster', views.umaSkillMasterViewSet)
# router.register('umaCardMaster', views.umaCardMasterViewSet)
# router.register('umaCardSkillMaster', views.umaCardSkillMasterViewSet)
# router.register('umaCardMessageMaster', views.umaCardMessageMasterViewSet)
# router.register('umaWhiteFactor', views.umaWhiteFactorViewSet)


app_name = 'rosterApp'

urlpatterns = [
    # =========勤怠管理画面用=========
    path('login/', RosterLoginView.as_view(), name="login"),
    path('login/ajaxlogincheck/', ajax_roster_login, name="ajaxlogincheck"),
    path('loginList/<str:uid>/<str:pwd>/', roster_list, name="loginList"),
    path('logininput/', RosterLoginInputView.as_view(), name="loginInput"),
    path('change/', RosterChangeView.as_view(), name="change"),
    # =========ウマ娘用ツール画面=========
    # メニュー画面
    path('umacomptool/', UmaCompToolView.as_view(), name="umacomptool"),
    # カードマスタ
    path('searchcardmaster/<int:typeno>/', umaCardMasterLoad, name="searchcardmaster"),
    # カードスキルマスタ
    path('cardskillmaster/<int:typeno>/', umaCardSkillMasterLoad, name="cardskillmaster"),
    # カードメッセージマスタ
    path('searchcardmessegemaster/<int:typeno>/', umaCardMessageMasterLoad, name="searchcardmessegemaster"),
    # スキルマスタ
    path('searchskillmaster/<int:typeno>/', umaSkillMasterLoad, name="searchskillmaster"),
    # 固有ボーナスマスタ
    path('searchuniquebonusmaster/<int:typeno>/', umaCardUniqueBonusLoad, name="searchuniquebonusmaster"),
    # 白因子マスタ
    path('searchwhitefactormaster/', umaWhiteFactorLoad, name="searchwhitefactormaster"),
    # 育成ウママスタ
    path('searchumamaster/',umaMasterLoad, name="searchwhitefactormaster"),
    # スキル詳細マスタ
    path('searchskilldetailmaster/',umaSkillDetailMasterLoad, name="searchwhitefactormaster"),
    # スキル評価マスタ
    path('seearchcardevaluationmaster/',umaSkillEvaluationMasterLoad, name="searchwhitefactormaster"),
    # =========管理画面=========
    path('admin/', admin.site.urls),
    # =========mongo管理画面用=========
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # =========テスト確認用=========
    path('aboutus/', AboutView.as_view(), name="about")
]

# 〓 memo 〓
# 〓〓〓〓〓各ユーザー画面〓〓〓〓〓
# ■■■出勤登録画面（出勤、退勤）■■■■
# →デフォルトで表示
# (遷移先)
# →出退勤変更要請（出勤、退勤時間、有給、体調不良等変更）
# →出勤日時と月ごとの出退勤時間の確認画面(備考入力して登録も可能)
# ■■■出退勤月検索画面■■■
# →出退勤月結果画面へ遷移する
# ■■■出退勤月結果画面へ遷移する■■■
# →日付単位で変更を行い出退勤変更依頼要請一覧画面へ遷移する
# ■■■出退勤変更依頼要請一覧■■■
# 出退勤変更依頼要請中の一覧画面をステータス別に表示する
#
# ■■■時刻変更要請依頼■■■
# →日付を指定して、出勤時間、退勤時間、ステータス(出勤、有給、休日)
#
# 〓〓〓〓〓管理者画面〓〓〓〓〓
# ■■■管理画面■■■
# →別URLとする(/admin
# ■■■ユーザー登録画面(住所、氏名、年齢、性別、役職(課長、部長、パートなど))■■■
# 出退勤変更依頼受付画面
# →変更依頼を日時別に承認するボタン、却下あり
# ■■■ユーザー別出退勤検索画面■■■
# →ユーザーと対象年月をドロップダウン表示
# ■■■ユーザー別出退勤結果画面■■■
# →各ユーザーの年月出退勤を月単位で表示する
# →各項目を自由に変更可能
# →入力漏れがないかチェックするボタンを追加する
# 〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
