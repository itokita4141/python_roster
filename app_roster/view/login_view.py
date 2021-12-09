import json
import sys
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import TemplateView  # テンプレートタグ
# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from .models import user, attendance
from ..models import user, attendance
# sql alchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import sys
# sys.path.append("/app_roster/db/config")
from setting_alchemy import Base
from setting_alchemy import ENGINE
# from setting_alchemy import DATABASE
from setting_alchemy import session
# sys.path.append("/app_roster/db/model")
from users import *
from attendances import *

# ======画面遷移==================
# ログイン
# ===============================
def ajax_roster_login(request):
    print("ajax_roster_login")
    return

def roster_login(request):
    returnMessageParams = {
        'errorMessage': 'dummy'
    }
    # フォーム入力のユーザーID・パスワード取得
    uid = request.GET.get('txt_userid')
    pwd = request.GET.get('txt_password')
    # 未入力がある場合は抜ける
    # if len(uid) == 0 or len(pwd) == 0:
    #     returnMessageParams["errorMessage"] = "ユーザーIDまたはパスワードが入力されていません。<br/>入力してください。"
    #     return render(request, "../../login", returnMessageParams)
    print("〓〓〓〓〓〓〓")
    print("ユーザーID="+uid)
    print("password="+pwd)
    print("〓〓〓〓〓〓〓")
    # userテーブル読み込み
    usersListCount = session.query(Users).filter(Users.email == uid, Users.password == pwd).count()
    # usersListCount2 = session.query(Users).all()
    print("=======================")
    print("users.count="+str(usersListCount))
    print("=======================")
    # ログインチェック
    if (usersListCount == 1):
        return redirect("../../input")
    if usersListCount == 0:
        returnMessageParams["errorMessage"] = 'ログインIDまたはパスワードが間違っています。'
        return render(request, "roster_login.html", {'data_json': returnMessageParams})
        # return render(request, "roster_login.html", {'data_json': json.dumps(returnMessageParams)})
        # return redirect(request.META['HTTP_REFERER']) # 元のURLに戻す
    elif(usersListCount > 1):
        returnMessageParams["errorMessage"] = '複数ユーザーのログインID、パスワードが一致しています。' \
                                              '<br/>データ不正のため運営に連絡してください。<br/>itokita41@gmail.com'
        return render(request, "roster_login.html", {'data_json': returnMessageParams})
        # return render(request, "roster_login.html", {'data_json': json.dumps(returnMessageParams)})
        # return redirect(request.META['HTTP_REFERER']) # 元のURLに戻す
