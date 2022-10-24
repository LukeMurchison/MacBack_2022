
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("near_hundred/<int:num>/", near_hundred),
    path("string_splosion/<str:input>/", string_splosion),
    path("cat_dog/<str:input>/", cat_dog),
    path("lone_sum/<int:a>/<int:b>/<int:c>/", lone_sum),
]
