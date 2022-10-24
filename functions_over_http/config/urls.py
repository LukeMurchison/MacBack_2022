
from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hey/<name>', hello_view),
    path('age-in/<int:end>/<int:birthyear>', how_old),
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>', take_order),
]
