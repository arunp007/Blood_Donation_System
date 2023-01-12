from django.shortcuts import render
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
