from django.shortcuts import render
from urllib3 import HTTPResponse
from django.http import HttpResponse

# Create your views here.
def helloworldappview(request):
    return HttpResponse('app is called ♪')