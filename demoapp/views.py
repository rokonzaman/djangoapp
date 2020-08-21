from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hi(request):
    return render(request,'demoapp/index.html')