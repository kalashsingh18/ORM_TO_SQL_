from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def check(request):
    return render(request,"converter/converterUI.html")
def mainconverter(request):
    if request.method=="POST":
        print(request.POST)
        return HttpResponse("the method is post")
    if request.method=="GET":
        return HttpResponse("jhyy")
