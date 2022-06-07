from django.shortcuts import render
from django.http import HttpResponse


def admin(request):
    return render(request, 'adminpage.html')

def adminnotification(request):
    return render(request, 'admin_notification.html')
