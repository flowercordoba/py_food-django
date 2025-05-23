from django.shortcuts import render
from django.http import HttpResponse

def Home(req):
   return HttpResponse('hola mundo')

