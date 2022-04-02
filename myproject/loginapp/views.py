from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def donorlogin(request):
    return render(request, 'donorlogin.html')

def hospitallogin(request):
    return render(request, 'hospitallogin.html')

def recipientlogin(request):
    return render(request, 'recipientlogin.html')

def admin(request):
    return render(request, 'adminlogin.html')
