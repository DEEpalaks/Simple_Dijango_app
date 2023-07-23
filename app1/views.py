from django.shortcuts import render
from django.http import HttpResponse
def view1(request):
    mes='<h1>Hi there I am using Whatsapp</h1>'
    return HttpResponse(mes)
def view2(request):
    meg='<h1>No one is perfect</h1>'
    return (HttpResponse(meg))


# Create your views here.
