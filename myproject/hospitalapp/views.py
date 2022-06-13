from urllib.request import Request
from django.shortcuts import render
from.models import *

def hospital(request):
    return render(request,'hospitalapp.html')

def hospitalsearch(request):
    return render(request, 'hospital_search.html')

def hospitalnotification(request):
    return render(request, 'hospital_notification.html')

def hospitalcamp(request):
    if request.method == 'POST':
        camp = request.POST['camp']
        date = request.POST['date']
        address = request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        details = Camps(camp = camp,date = date,address = address,state = state,district = district,name = name,phone = phone,email = email)
        details.save()
    return render(request, 'hospital_camp.html')

def camptable(request):
    camp_details = Camps.objects.all()
    return render(request, 'camptable.html', {'details' : camp_details})
