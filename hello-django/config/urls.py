
from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello_view),
    path("roll-die/<int:sides>/", roll_die_view),
    path("random-between/<int:lo>/<int:hi>", ran_between),
]
