from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def near_hundred(request, num):
    new_num = abs(num - 100)
    #return HttpResponse(new_num)
    if new_num >= 10 and new_num <= 10:
        return HttpResponse(True)
    elif new_num >= 110 and new_num <= 110:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
        
def string_splosion(request, input):
    result = ""
    for x in range(len(input)):
        result = result + input[:x+1]
    return HttpResponse(result)

def cat_dog(request, input):
    count_cat = 0
    count_dog = 0
    for x in range(len(input)-2):
        if input[x:x+3] == 'dog':
            count_dog += 1
        if input[x:x+3] == 'cat':
            count_cat += 1
    return HttpResponse(count_cat == count_dog)

def lone_sum(request, a, b, c):
  if a == b == c:
    return HttpResponse(0)
  if b == c:
    return HttpResponse(a)
  if a == c:
    return HttpResponse(b)
  if a == b:
    return HttpResponse(c)
  return HttpResponse(a+b+c)