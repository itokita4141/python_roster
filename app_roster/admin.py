# from django.contrib import admin
#
# # Register your models here.
from django.contrib import admin
from .models import Post,user,attendance

admin.site.register(user)
admin.site.register(attendance)