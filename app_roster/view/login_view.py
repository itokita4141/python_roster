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
def ajax_roster_login(request):
    print("ajax_roster_login")
    returnMessageParams = {
        'errorMessage': 'dummy'
    }
    # フォーム入力のユーザーID・パスワード取得
    uid = request.POST.get("uid", False)
    pwd = request.POST.get("pwd", False)
    if request.method == 'POST':
        print("〓〓〓〓〓〓〓")
        print("ユーザーID="+uid)
        print("password="+pwd)
        print("〓〓〓〓〓〓〓")
        # pymongo
        mongo = settingPymongo('rosterdb', 'app_roster_users')
        find = mongo.find(filter={'name': uid, 'password': pwd})
        usersListCount = find.count()
        # print('count=='+str(usersListCount))
        # try:
        #     doc = find.next
        #     for doc in find:
        #         print(doc['id'])
        #         print(doc['name'])
        #         print(doc['password'])
        # except StopIteration:
        #     pass
        # ログインチェック
        if usersListCount == 0:
            returnMessageParams = {'userId': '',
                                    'name': '',
                                    'sex': '',
                                    'contract': '',
                                    'tell': '',
                                    'email': '',
                                    'errorMessage': 'ログインIDまたはパスワードが間違っています',
                                    'result': 'ng',
            }
            render(request, "roster_login.html", returnMessageParams)
            return JsonResponse(returnMessageParams)
        elif(usersListCount > 1):
            returnMessageParams = {'userId': '',
                                    'name': '',
                                    'sex': '',
                                    'contract': '',
                                    'tell': '',
                                    'email': '',
                                    'errorMessage': '複数ユーザーのログインID、パスワードが一致しています。' \
                                    '<br/>データ不正のため運営に連絡してください。<br/>itokita41@gmail.com',
                                    'result': 'ng',
            }
            render(request, "roster_login.html", returnMessageParams)
            return JsonResponse(returnMessageParams)
        elif (usersListCount == 1):
            returnMessageParams = {'userId': '',
                                    'name': '',
                                    'sex': '',
                                    'contract': '',
                                    'tell': '',
                                    'email': '',
                                    'errorMessage': '',
                                    'result': 'ok',
            }
            return JsonResponse(returnMessageParams)
    elif request.method == 'GET':
        print("通信に失敗しました。GET送信になっています。")

#   # 〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
#   # 処理参考用 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#   # 〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
#   findone = mongo.find_one()
#   print('-----------------find_One-----------------')
#   print(type(findone))
#   print(findone)
#
#   find = mongo.find()
#   print('-------------------find-------------------')
#   print(type(find))
#   for doc in find:
#       print(doc)
#   print('-----------------find filter-----------------')
#   find = mongo.find(filter={'id': 3})
#   for doc in find:
#       print(doc)
#       print(doc['name'])
#   print('-----------------find filters-----------------')
#   find = mongo.find(filter={'id':3, 'name': 'taka'})
#   print(find.count()) # 件数
#   for doc in find:
#       print(doc)
#   print('-----------------sort-------------------------')
#   find = mongo.find(sort=[('id', ASCENDING)])
#   for doc in find:
#       print(doc)
#   print('-----------------cursol sort-------------------------')
#   find = mongo.find()
# # for doc in find.sort([('salary', DESCENDING), ('name', ASCENDING)]):
# #   for doc in find.sort([('name', DESCENDING)]):
# #       print(doc)
#   print('-----------------nextループ-------------------------')
#   try:
#       doc = find.next()
#       while doc != None:
#           print(doc)
#           doc = find.next()
#   except StopIteration:
#       pass
#
#   # mongoengine
#   print(Users.objects.all())
#   usersAllData = Users.objects.all()
#   # print("Usersのデータ数=" . str(usersAllData))
#   counter = 0
#   for usersData in usersAllData:
#       print(counter)
#       print(usersData.userId)
#       counter = counter + 1
#
#   usersListCount = counter
#   # mongoalchemy
#   # ・flaskのみ？
#   # userテーブル読み込み
#   # usersListCount = session.query(Users).filter(Users.email == uid, Users.password == pwd).count()
#   # usersListCount2 = session.query(Users).all()
#   # print("=======================")
#   print("users.count="+str(usersListCount))
# print("=======================")
#   # 〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
#   # 処理参考用 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
#   # 〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
