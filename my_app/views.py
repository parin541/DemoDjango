from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, Everyone from django application from the GitHub!')

