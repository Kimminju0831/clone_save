from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'blog/main.html')

def siteMain(reqeust):
    return render(request, 'siteMain.html')

def detail(request):
    return render(request, 'blog/detail.html')

def credit(request):
    return render(request, 'blog/credit.html')

def main_map(request):
    return render(request, 'blog/map.html')