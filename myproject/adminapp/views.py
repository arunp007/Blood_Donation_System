from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import *


def admin(request):
    return render(request, 'adminpage.html')

def admin_notification(request):
    message_data = Message.objects.all()
    return render(request, 'admin_notification.html', {'message': message_data})

def donor_notification(request):
    message_data = Message.objects.all()
    return render(request, 'donor_notification.html', {'message' : message_data})

def recipient_notification(request):
    message_data = Message.objects.all()
    return render(request, 'recipient_notification.html', {'message': message_data})

def hospital_notification(request):
    message_data = Message.objects.all()
    return render(request, 'hospital_notification.html', {'message': message_data})
    
def notification(request):
    if request.method == 'POST':
        message = request.POST['messages']
        data = Message(messages = message)
        data.save()
    return render(request, 'notification.html')


def add_donor(request):
    if request.method == 'POST':
        name = request.POST['name']
        blood = request.POST['blood']
        location = request.POST['location']
        phone = request.POST['phone']
        donor_data = Donordata(name = name, blood = blood, location = location, phone = phone)
        donor_data.save()
    return render(request, 'add_donor.html')

def donor_table(request):
    donor_data = Donordata.objects.all()
    return render(request, 'donor_table.html', {'donor': donor_data})

def delete(request,id):
    Donordata.objects.get(id = id).delete()
    return redirect('donor_table')

def update(request,id):
    update_data = ""
    if request.method == 'POST':
        name = request.POST['name']
        blood = request.POST['blood']
        location = request.POST['location']
        phone = request.POST['phone']
        Donordata.objects.filter(id = id).update(name = name, blood = blood, location = location, phone = phone)
        return redirect('donor_table')
    else:
        update_data = Donordata.objects.get(id = id)
        return render(request, 'add_donor.html', {'update': update_data})

def donor(request):
    donor_data = Donordata.objects.all()
    return render(request, 'donor.html', {'donor': donor_data})


