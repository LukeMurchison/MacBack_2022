from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse

def hello_view(request, name):
    return HttpResponse(f"Hello, {name}!")

def how_old(request, end, birthyear):
    age = abs(birthyear - end)
    return HttpResponse(age)

def take_order(request, burgers, fries, drinks):
    burger_total = burgers * 4.5
    fries_total = fries * 1.5
    drinks_total = drinks * 1
    total = burger_total + fries_total + drinks_total
    return HttpResponse(f"{str(total)}")