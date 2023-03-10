from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def dj(request):
    return HttpResponse('<h1> is the best allrounder<h1/>')