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
from django.contrib import admin
from django.urls import path

# from .views import IndexView, AboutView, RosterLoginInputView, RosterLoginView, RosterInputView, RosterListView, RosterChangeView\
    # , MsgboxView
from .views import AboutView, RosterLoginInputView, RosterLoginView, RosterInputView, RosterListView, RosterChangeView\

urlpatterns = [
    path('login/', RosterLoginView.as_view(), name="login"),
    path('logininput/', RosterLoginInputView.as_view(), name="loginInput"),
    path('list/', RosterListView.as_view(), name="list"),
    path('input/', RosterInputView.as_view(), name="input"),
    path('change/', RosterChangeView.as_view(), name="change"),
    # path('msgbox/', MsgboxView.as_view(), name="msgbox"),
    # 管理画面
    path('admin/', admin.site.urls),
    # テスト確認用
    path('aboutus/', AboutView.as_view(), name="about"),
    # 廃止
    # path('', IndexView.as_view(), name="index"),
]
