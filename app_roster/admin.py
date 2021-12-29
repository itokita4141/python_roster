# from django.contrib import admin
#
# # Register your models here.
from django.contrib import admin
# from .models import Post,user,attendance
# from .models import Question, Choice, users
from .models import Users, Attendances

admin.site.register(Users)
admin.site.register(Attendances)
