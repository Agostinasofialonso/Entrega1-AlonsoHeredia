from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def start (request):
    return HttpResponse('<h1>First view</h1>')
