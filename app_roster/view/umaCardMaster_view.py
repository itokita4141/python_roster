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
    mongo = settingPymongo('rosterdb', 'app_roster_umacardmaster')
    find = mongo.find(filter={'cardMasterId': 1})
    count = find.count()

    for doc in find:
        returnMessageParams = {'cardMasterId' : doc['cardMasterId'],
                               'cardName' : doc['cardName']
                               }
        print(doc['cardMasterId'])
        print(doc['cardName'])

    return render(request, 'SearchCardMasterView.html', returnMessageParams)





