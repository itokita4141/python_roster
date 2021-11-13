from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import roster.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path("admin/", admin.site, site_urls),
#     path("", include("testproject.uris")),
# ]

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
]
