from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello World!')

def altHomePage(request):
    return HttpResponse('This is alt homePage!')
    