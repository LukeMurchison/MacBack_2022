
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("", land),
    path("<input>/", home),
    path("admin/", admin.site.urls),
]
