import json
from django.http import JsonResponse
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
    returnMessageParams = {
        'errorMessage': 'dummy'
    }
    # フォーム入力のユーザーID・パスワード取得
    # uid = request.POST.get('txt_userid')
    # pwd = request.POST.get('txt_password')
    # json_data = request.POST["uid"]
    # json_data = request.POST["pwd"]
    # data = json.dumps(json_data)
    uid = request.POST.get("uid", False)
    pwd = request.POST.get("pwd", False)

    if request.method == 'POST':
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
            returnMessageParams = {
                'errorMessage': '',
                'result': 'ok',
            }
            # returnMessageParams["errorMessage"] = ''
            # redirect("../../input")
            return JsonResponse(returnMessageParams)
        if usersListCount == 0:
            returnMessageParams = {
                'errorMessage': 'ログインIDまたはパスワードが間違っています',
                'result': 'ng',
            }
            # returnMessageParams["errorMessage"] = 'ログインIDまたはパスワードが間違っています。'
            render(request, "roster_login.html", returnMessageParams)
            return JsonResponse(returnMessageParams)
            # return render(request, "roster_login.html", {'data_json': json.dumps(returnMessageParams)})
            # return redirect(request.META['HTTP_REFERER']) # 元のURLに戻す
        elif(usersListCount > 1):
            returnMessageParams = {
                'errorMessage': '複数ユーザーのログインID、パスワードが一致しています。' \
                                '<br/>データ不正のため運営に連絡してください。<br/>itokita41@gmail.com',
                'result': 'ng',
            }
            # returnMessageParams["errorMessage"] = '複数ユーザーのログインID、パスワードが一致しています。' \
            #                                       '<br/>データ不正のため運営に連絡してください。<br/>itokita41@gmail.com'
            render(request, "roster_login.html", returnMessageParams)
            return JsonResponse(returnMessageParams)
            # return render(request, "roster_login.html", {'data_json': json.dumps(returnMessageParams)})
            # return redirect(request.META['HTTP_REFERER']) # 元のURLに戻す
    elif request.method == 'GET':
        print("通信に失敗しました。GET送信になっています。")


# def roster_login(request):
#     returnMessageParams = {
#         'errorMessage': 'dummy'
#     }
#     # フォーム入力のユーザーID・パスワード取得
#     uid = request.GET.get('txt_userid')
#     pwd = request.GET.get('txt_password')
#     # 未入力がある場合は抜ける
#     # if len(uid) == 0 or len(pwd) == 0:
#     #     returnMessageParams["errorMessage"] = "ユーザーIDまたはパスワードが入力されていません。<br/>入力してください。"
#     #     return render(request, "../../login", returnMessageParams)
#     print("〓〓〓〓〓〓〓")
#     print("ユーザーID="+uid)
#     print("password="+pwd)
#     print("〓〓〓〓〓〓〓")
#     # userテーブル読み込み
#     usersListCount = session.query(Users).filter(Users.email == uid, Users.password == pwd).count()
#     # usersListCount2 = session.query(Users).all()
#     print("=======================")
#     print("users.count="+str(usersListCount))
#     print("=======================")
#     # ログインチェック
#     if (usersListCount == 1):
#         return redirect("../../input")
#     if usersListCount == 0:
#         returnMessageParams["errorMessage"] = 'ログインIDまたはパスワードが間違っています。'
#         return render(request, "roster_login.html", {'data_json': returnMessageParams})
#         # return render(request, "roster_login.html", {'data_json': json.dumps(returnMessageParams)})
#         # return redirect(request.META['HTTP_REFERER']) # 元のURLに戻す
#     elif(usersListCount > 1):
#         returnMessageParams["errorMessage"] = '複数ユーザーのログインID、パスワードが一致しています。' \
#                                               '<br/>データ不正のため運営に連絡してください。<br/>itokita41@gmail.com'
#         return render(request, "roster_login.html", {'data_json': returnMessageParams})
#         # return render(request, "roster_login.html", {'data_json': json.dumps(returnMessageParams)})
#         # return redirect(request.META['HTTP_REFERER']) # 元のURLに戻す