from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def donor(request):
    return render(request, 'donor.html')

def recipient(request):
    return render(request, 'recipient.html')

def hospital(request):
    return render(request, 'hospital.html')
