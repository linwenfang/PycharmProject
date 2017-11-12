from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
def index(request):
    contex={'title':'Django首页','list':range(10)}
    return render(request,'booktest/index.html',contex)
def book(request):
    list=BookInfo.objects.all()
    contex={'booklist':list,'title':'BookList'}
    return render(request,'booktest/book.html',contex)
def detail(request,id):
    list=BookInfo.objects.get(id=id).detailinfo_set.all()
    contex={'listdetail':list,'title':'Detail'}
    return render(request,'booktest/detail.html',contex)
