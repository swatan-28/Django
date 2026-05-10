from django.shortcuts import render
from django.http import HttpResponse

def renderSomething(req):
    return render(req,"index.html")

def aboutSomething(req):
    return HttpResponse("About Page -> fn written in app->views")
# Create your views here.
