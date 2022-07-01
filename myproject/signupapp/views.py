from django.shortcuts import render
from django.http import HttpResponse
from.models import *


def donor(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        blood = request.POST['bloodgroup']
        aadhaar = request.POST['aadhaar']
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']
        gender = request.POST['gender']
        address = request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        pin = request.POST['pincode']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        auth = request.POST['auth']
        donor_data = Donors(fname=fname, lname=lname, blood=blood, aadhaar=aadhaar, day=day, month=month, year=year, gender=gender, address=address, state=state, district=district, pin=pin, phone=phone, email=email, password=password, cpassword=cpassword, auth=auth)
        donor_data.save()
    return render(request, 'donor.html')

def donor_details(request):
    donor_details = Donors.objects.all()
    return render(request, 'donor_details.html', {'donor': donor_details})

def donor_data(request):
    donor_info = Donors.objects.all()
    return render(request, 'donor_data.html', {'info': donor_info})

def recipient(request):
    return render(request, 'recipient.html')

def hospital(request):
    return render(request, 'hospital.html')
