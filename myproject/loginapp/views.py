from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import *

def donor_signup(request):
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
        location = request.POST['location']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        donor_details = Donors(fname = fname, lname = lname, blood = blood, aadhaar = aadhaar, day = day, month = month, year = year, gender = gender, address = address, state = state, district = district, location = location, phone = phone, email = email, password = password, cpassword = cpassword)
        donor_details.save()
    return render(request, 'donor_signup.html')

def donors(request):
    donor_data = Donors.objects.all()
    return render(request, 'donors.html', {'data': donor_data})

def donors_update(request, id):
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
        location = request.POST['location']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        Donors.objects.filter(id = id).update(fname = fname, lname = lname, blood = blood, aadhaar = aadhaar, day = day, month = month, year = year, gender = gender, address = address, state = state, district = district, location = location, phone = phone, email = email, password = password, cpassword = cpassword)
        return redirect('donors')

    else:
        update_data = Donors.objects.get(id = id)
        return render(request, 'donor_signup.html', {'update': update_data})

def donors_delete(request, id):
    Donors.objects.get(id = id).delete()
    return redirect('donors')

def recipient_signup(request):
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
        location = request.POST['location']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        recipient_details = Recipients(fname = fname, lname = lname, blood = blood, aadhaar = aadhaar, day = day, month = month, year = year, gender = gender, address = address, state = state, district = district, location = location, phone = phone, email = email, password = password, cpassword = cpassword)
        recipient_details.save()
    return render(request, 'recipient_signup.html')

def recipients(request):
    recipient_data = Recipients.objects.all()
    return render(request, 'recipients.html', {'data': recipient_data})

def recipients_update(request, id):
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
        location = request.POST['location']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        Recipients.objects.filter(id = id).update(fname = fname, lname = lname, blood = blood, aadhaar = aadhaar, day = day, month = month, year = year, gender = gender, address = address, state = state, district = district, location = location, phone = phone, email = email, password = password, cpassword = cpassword)
        return redirect('recipients')

    else:
        update_data = Recipients.objects.get(id = id)
        return render(request, 'recipient_signup.html', {'update': update_data})

def recipients_delete(request, id):
    Recipients.objects.get(id = id).delete()
    return redirect('recipients')


def hospital_signup(request):
    if request.method == 'POST':
        hname = request.POST['hname']
        address = request.POST['address']
        location = request.POST['location']
        state = request.POST['state']
        district = request.POST['district']
        pin = request.POST['pincode']
        phone  = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        hospital_details = Hospitals(hname = hname, address = address, location = location, state = state, district = district, pin = pin, phone = phone, email = email, password = password, cpassword = cpassword)
        hospital_details.save()
    return render(request, 'hospital_signup.html')

def hospitals(request):
    hospital_data = Hospitals.objects.all()
    return render(request, 'hospitals.html', {'data': hospital_data})

def hospitals_update(request, id):
    if request.method == 'POST':
        update_data = ""
        hname = request.POST['hname']
        address = request.POST['address']
        location = request.POST['location']
        state = request.POST['state']
        district = request.POST['district']
        pin = request.POST['pincode']
        phone  = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        Hospitals.objects.filter(id = id).update(hname = hname, address = address, location = location, state = state, district = district, pin = pin, phone = phone, email = email, password = password, cpassword = cpassword)
        return redirect('hospitals')

    else:
        update_data = Hospitals.objects.get(id = id)
        return render(request, 'hospital_signup.html', {'update': update_data})

def hospitals_delete(request, id):
    Hospitals.objects.get(id = id).delete()
    return redirect('hospitals')

def donorlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            current_user = Donors.objects.get(email = email, password = password)
            request.session['xyz'] = current_user.id
            return redirect('donor_home')

        except Donors.DoesNotExist:
            return render(request, 'donorlogin.html', {'message': 'Email Id And Password Is Wrong'})
    
    return render(request, 'donorlogin.html')

def donor_logout(request):
    request.session.flush()
    return redirect('donorlogin')

def hospitallogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            Hospitals.objects.get(email = email, password = password)
            return redirect('hospital_home')

        except Hospitals.DoesNotExist:
            return render(request, 'hospitallogin.html', {'message': 'Email Id And Password Is Wrong'}) 
    return render(request, 'hospitallogin.html')

def hospital_logout(request):
    request.session.flush()
    return redirect('hospitallogin')

def recipientlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            Recipients.objects.get(email = email, password = password)
            return redirect('recipient_home')

        except Recipients.DoesNotExist:
            return render(request, 'recipientlogin.html', {'message': 'Email Id And Password Is Wrong'})
    return render(request, 'recipientlogin.html')

def recipient_logout(request):
    request.session.flush()
    return redirect('recipientlogin')

def admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            current_user = Admin.objects.get(username = username, password = password)
            request.session['xyz'] = current_user.id
            return redirect('admin_home')

        except Admin.DoesNotExist:
            return render(request, 'adminlogin.html', {'message': 'Username And Password Is Wrong'})
            
    return render(request, 'adminlogin.html')


def admin_logout(request):
    request.session.flush()
    return redirect('adminlogin')
