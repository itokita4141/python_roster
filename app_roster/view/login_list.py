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
from ..models import Users, Attendances, Logs
# sql alchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import sys
from setting_alchemy import Base
from setting_alchemy import ENGINE
from setting_alchemy import session
from rest_framework import viewsets
from app_roster.seliarizers import UsersSerializer, AttendancesSerializer,LogsSerializer
# pymongo
from pymongo import MongoClient
sys.path.append("app_roster/db/mongodb/config")
from setting_pymongo import settingPymongo
from pymongo import ASCENDING
from pymongo import DESCENDING

# ======画面遷移==================
# ログイン
# ===============================
# from django.views import View
def roster_list(request,uid,pwd):
    # def get(self, request):
    print("roster_list start")
    returnMessageParams = {'errorMessage': 'dummy'}
    # フォーム入力のユーザーID・パスワード取得
    # uid = request.POST.get("uid", False)
    # pwd = request.POST.get("pwd", False)
    if request.method == 'GET':
        # print("〓〓〓〓〓〓〓")
        # print("ユーザーID="+uid)
        # print("password="+pwd)
        # print("〓〓〓〓〓〓〓")
        # pymongo
        mongo = settingPymongo('rosterdb', 'app_roster_users')
        find = mongo.find(filter={'name': uid, 'password': pwd})
        # user情報を取得
        count = find.count()
        if count == 0:
            returnParams = {'userId': '',
                            'name': '',
                            'sex': '',
                            'contract': '',
                            'tell': '',
                            'email': '',
                            'errorMessage': 'ユーザー情報が見つかりません。',
                            'result': 'ng',
                            }
            return render (request, 'roster_list.html', returnMessageParams)
        elif count == 1:
            for doc in find:
                returnParams = {'userId': doc['userId'],
                                'name': doc['name'],
                                'sex': doc['sex'],
                                'contract': doc['contract'],
                                'tell': doc['tell'],
                                'email': doc['email'],
                                'errorMessage': '',
                                'result': '',
                                }
            return render(request,'roster_list.html', returnParams)
        elif count > 1:
            returnParams = {'userId': '',
                            'name': '',
                            'sex': '',
                            'contract': '',
                            'tell': '',
                            'email': '',
                            'errorMessage': 'ユーザー情報が複数形見つかりました。',
                            'result': 'ng',
                            }
            return render(request, 'roster_list.html', returnMessageParams)
        # ログインチェック
    elif request.method == 'GET':
        print("通信に失敗しました。GET送信になっています。")
    print('loginList post end')

    # def post(self, request):
    #     print('loginList post start')
    #     print('loginList post end')
