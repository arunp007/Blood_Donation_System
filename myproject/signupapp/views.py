from django.shortcuts import render, redirect
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
        authentication = request.POST['auth']
        donor_data = Donors(fname = fname, lname = lname, blood = blood, aadhaar = aadhaar, day = day, month = month, year = year, gender = gender, address = address, state = state, district = district, pin = pin, phone = phone, email = email, password = password, cpassword = cpassword, authentication = authentication)
        donor_data.save()
    return render(request, 'donor.html')

def donor_details(request):
    donor_details = Donors.objects.all()
    return render(request, 'donor_details.html', {'donor': donor_details})

def donor_data(request):
    donor_info = Donors.objects.all()
    return render(request, 'donor_data.html', {'info': donor_info})

def donor_update(request,id):
    if request.method == 'POST':
        update_data = ""
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
        authentication = request.POST['auth']
        Donors.objects.filter(id = id).update(fname = fname, lname = lname, blood = blood, aadhaar = aadhaar, day = day, month = month, year = year, gender = gender, address = address, state = state, district = district, pin = pin, phone = phone, email = email, password = password, cpassword = cpassword, authentication = authentication)
        return redirect('donor_details')

    else:
        update_data = Donors.objects.get(id = id)
        return render(request, 'donor.html', {'update': update_data })

def donor_delete(request, id):
    Donors.objects.get(id = id).delete()
    return redirect('donor_details')

def recipient(request):
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
        authentication = request.POST['auth']
        recipient_data = Recipients(fname = fname, lname = lname, blood = blood, aadhaar = aadhaar, day = day, month = month, year = year, gender = gender, address = address, state = state, district = district, pin = pin, phone = phone, email = email, password = password, cpassword = cpassword, authentication = authentication)
        recipient_data.save()
    return render(request, 'recipient.html')

def recipient_details(request):
    recipient_details = Recipients.objects.all()
    return render(request, 'recipient_details.html', {'recipient': recipient_details })

def recipient_update(request,id):
    if request.method == 'POST':
        update_data = ""
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
        authentication = request.POST['auth']
        Recipients.objects.filter(id = id).update(fname = fname, lname= lname, blood = blood, aadhaar = aadhaar, day = day, month = month, year = year, gender = gender, address = address, state = state, district = district, pin = pin, phone = phone, email = email, password = password, cpassword = cpassword, authentication = authentication)
        return redirect('recipient_details')

    else:
        update_data = Recipients.objects.get(id = id)
        return render(request, 'recipient.html', {'update' : update_data})

def recipient_delete(request,id):
    Recipients.objects.get(id = id).delete()
    return redirect('recipient_details')

def hospital(request):
    if request.method == 'POST':
        hname = request.POST['hname']
        address = request.POST['address']
        location = request.POST['location']
        state = request.POST['state']
        district = request.POST['district']
        pin = request.POST['pincode']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        authentication = request.POST['auth']
        hospital_data = Hospitals(hname = hname, address = address, location = location, state = state, district = district, pin = pin, phone = phone, email = email, password = password, cpassword = cpassword, authentication = authentication)
        hospital_data.save()
    return render(request, 'hospital.html')


def hospital_details(request):
    hospital_details = Hospitals.objects.all()
    return render(request, 'hospital_details.html', {'hospital': hospital_details })

def hospital_update(request,id):
    if request.method == 'POST':
        update_data = ""
        hname = request.POST['hname']
        address = request.POST['address']
        location = request.POST['location']
        state = request.POST['state']
        district = request.POST['district']
        pin = request.POST['pincode']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        authentication = request.POST['auth']
        Hospitals.objects.filter(id = id).update(hname = hname, address = address, location = location, state = state, district = district, pin = pin, phone = phone, email = email, password = password, cpassword = cpassword, authentication = authentication)
        return redirect('hospital_details')
    
    else:
        update_data = Hospitals.objects.get(id = id)
        return render(request, 'hospital.html', {'update': update_data})

def hospital_delete(request,id):
    Hospitals.objects.get(id = id).delete()
    return redirect('hospital_details')
