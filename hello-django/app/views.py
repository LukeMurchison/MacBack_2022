from http.client import HTTPResponse
import random
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_view(request):
    return HttpResponse(f"Hello World!")

def roll_die_view(request, sides):
    roll = random.randint(1,sides)
    return HttpResponse(roll)

def ran_between(request, lo, hi):
    return HttpResponse(random.randint(lo,hi))