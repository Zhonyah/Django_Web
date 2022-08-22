from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    return render(request, 'Mywebsite/index.html')

def mydata(request):
    return render (request,'Mywebsite/mydata.html')

def addnews(request):
    return render (request, 'Mywebsite/addnews.html')

def result(requser):
    name = request.post['name_news']
    detail = request.post['name_detail']
    print(name)
    print(detail)
    return render (requser, 'Mywebsite/result.html')
