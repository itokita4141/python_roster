from django.shortcuts import render
from django.views.generic import TemplateView

from django.shortcuts import render
from django.views.generic import TemplateView #テンプレートタグ
# from .forms import AccountForm, AddAccountForm #ユーザーアカウントフォーム
# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import user, attendance
# sql alchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

# ======画面遷移==================
# ログイン
# ===============================
def roster_login(request):
    users = user.objects.all()
    test = user.userId
    print("login") # どこに出力されてる？要確認
    # フォーム入力のユーザーID・パスワード取得
    userid = request.GET.get('userid')
    password = request.GET.get('password')
    # ユーザー認証
    if len(userid)!=0 and len(password)!=0 :
        # ホームページ遷移
        return redirect("../../input")
    # ユーザー認証失敗
    else:
        return HttpResponse("ログインIDまたはパスワードが間違っています")

# #ログアウト
# @login_required
# def Logout(request):
#     logout(request)
#     # ログイン画面遷移
#     return HttpResponseRedirect(reverse('Login'))
#
# #ホーム
# @login_required
# def home(request):
#     params = {"UserID":request.user,}
#     return render(request, "App_Folder2_HTML/home.html",context=params)
#
#新規登録
# class  AccountRegistration(TemplateView):
#
#     def __init__(self):
#         self.params = {
#         "AccountCreate":False,
#         "account_form": AccountForm(),
#         "add_account_form":AddAccountForm(),
#         }
#
#     #Get処理
#     def get(self,request):
#         self.params["account_form"] = AccountForm()
#         self.params["add_account_form"] = AddAccountForm()
#         self.params["AccountCreate"] = False
#         return render(request,"App_Folder_HTML/register.html",context=self.params)
#
#     #Post処理
#     def post(self,request):
#         self.params["account_form"] = AccountForm(data=request.POST)
#         self.params["add_account_form"] = AddAccountForm(data=request.POST)
#
#         #フォーム入力の有効検証
#         if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
#             # アカウント情報をDB保存
#             account = self.params["account_form"].save()
#             # パスワードをハッシュ化
#             account.set_password(account.password)
#             # ハッシュ化パスワード更新
#             account.save()
#
#             # 下記追加情報
#             # 下記操作のため、コミットなし
#             add_account = self.params["add_account_form"].save(commit=False)
#             # AccountForm & AddAccountForm 1vs1 紐付け
#             add_account.user = account
#
#             # 画像アップロード有無検証
#             if 'account_image' in request.FILES:
#                 add_account.account_image = request.FILES['account_image']
#
#             # モデル保存
#             add_account.save()
#
#             # アカウント作成情報更新
#             self.params["AccountCreate"] = True
#
#         else:
#             # フォームが有効でない場合
#             print(self.params["account_form"].errors)
#
#         return render(request,"App_Folder_HTML/register.html",context=self.params)

#     def post(self, request, *args, **kwargs):
#         print("post")
#         template_name = "roster_change_application.html"
#         context = {
#             'name': request.POST['name'],
#             'email': request.POST['email'],
#             'message': request.POST['message'],
#         }
#         return render(request, template_name, context)
# change = RosterChangeView.as_view()
#     # template_name = "roster_change_application.html"
#     # def get_context_data(self):
#     #     ctxt = super().get_context_data()
#     #     ctxt ["user"] = "testUser"
#     #     return ctxt

# ======画面遷移==================
# class IndexView(TemplateView):
#     template_name = "roster_login.html"
#     def get_context_data(self):
#         ctxt = super().get_context_data()
#         ctxt["username"] = "太郎"
#         return ctxt

# 出退勤登録画面
class RosterInputView(TemplateView):
    template_name = "roster_input.html"
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt ["user"] = "testUser"
        return ctxt

class RosterChangeView(TemplateView):
    def get(self, request, *args, **kwargs):
        print("get")
        template_name = "roster_change_application.html"
        context = {
            'message': "Hello World! from View!!",
        }
        return render(request, template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["skills"] = [
            "Python",
            "C++",
            "Javascript",
            "Rust",
            "Ruby",
            "PHP"
        ]
        ctxt["num_services"] = 1234567
        return ctxt

def some_view(request):
    if request.method == 'POST':
        # if 'attendance' in request.POST:
        #     # ボタン1がクリックされた場合の処理
        #     # hoge1()
        # elif 'departure' in request.POST:
        #     # ボタン2がクリックされた場合の処理
        #     # hoge2()
        if 'logout' in request.POST:
            logout()

class RosterLoginView(TemplateView):
    # ログイン画面
    print("RosterLoginView")
    template_name = "roster_login.html"
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt ["user"] = "testUser"
        return ctxt

# ログイン登録画面
class RosterLoginInputView(TemplateView):
    template_name = "roster_login_input.html"
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt ["user"] = "testUser"
        return ctxt

class RosterListView(TemplateView):
    template_name = "roster_list.html"
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["user"] = "testUser"
        return ctxt

class RosterUserInputView(TemplateView):
    template_name = "roster_change_application.html"
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["user"] = "testUser"
        return ctxt

class MsgboxView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {
            'message': "Hello World! from View!!",
        }
        return render(request,  "change.html", context)

    def post(self, request, *args, **kwargs):
        context = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }
        return render(request, 'change.html', context)
# hello = MsgboxView.as_view()

def logout():
    print("logout")
