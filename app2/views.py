from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime as d
def view1(request):
    mes='<h2>Ohiiiiiii</h2>'
    da=d.now()
    m=[1,2,3,4,5,6,7,8,9,10]
    dict1={'date':da,'lo':m}
    return render(request,'Templatesapp1/Html1.html',context=dict1)
def view2(request):
    mes='<h3>Meenuu</h3>'
    return HttpResponse(mes)


# Create your views here.
