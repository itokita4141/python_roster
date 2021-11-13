from django.shortcuts import render
from django.views.generic import TemplateView

class RosterLoginView(TemplateView):
    # ログイン画面
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

    def post(self, request, *args, **kwargs):
        print("post")
        template_name = "roster_change_application.html"
        context = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }
        return render(request, template_name, context)
change = RosterChangeView.as_view()
    # template_name = "roster_change_application.html"
    # def get_context_data(self):
    #     ctxt = super().get_context_data()
    #     ctxt ["user"] = "testUser"
    #     return ctxt

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

# class MsgboxView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         context = {
#             'message': "Hello World! from View!!",
#         }
#         return render(request,  "change.html", context)
#
#     def post(self, request, *args, **kwargs):
#         context = {
#             'name': request.POST['name'],
#             'email': request.POST['email'],
#             'message': request.POST['message'],
#         }
#         return render(request, 'change.html', context)
#
# hello = MsgboxView.as_view()

# ここはサンプル
class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "太郎"
        return ctxt

# ここはサンプル
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

def logout():
    print("logout")


