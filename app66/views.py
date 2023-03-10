from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def abd(request):
    return HttpResponse('<h1> is the best 360 batctsman <h1/>')