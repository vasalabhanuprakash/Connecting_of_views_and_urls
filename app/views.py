from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sample(request):
    return HttpResponse('<h1> Hellow World</h1>')