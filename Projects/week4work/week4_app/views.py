from django.shortcuts import render

# Create your views here.

def helloworld(request):
    return render(request,'Helloworld.html')

def block(request):
    return render(request,"parentblock.html")
