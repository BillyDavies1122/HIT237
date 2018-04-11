from django.shortcuts import render
from app_week6.models import customer
# Create your views here.
def home(request):
    return render(request, 'index.html')

def customer_details(request):
    result = customer.objects.order_by('phNumb')
    dataDict = {'customer':result}
    return render(request,'allCust.html',dataDict)

def singleCust(request ,ID):
    result = customer.objects.get(id=ID)
    pageData ={'customer':result}
    return render(request,'singleCust.html',pageData)
