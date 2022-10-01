from django.shortcuts import render
from.models import *

def recipient(request):
    return render(request,'recipientpage.html')

def recipientsearch(request):
    return render(request,'recipient_search.html')

def recipientbloodrequest(request):
    if request.method == 'POST':
        blood = request.POST['blood']
        name = request.POST['name']
        phone = request.POST['phone']
        location = request.POST['location']
        details = Blood(blood=blood,name=name,phone=phone,location=location)
        details.save()
    return render(request, 'recipient_bloodrequest.html')

def bloodrequest(request):
    bloodrequest = Blood.objects.all()
    return render(request, 'bloodrequest.html', {'details': bloodrequest})

def recipient_notification(request):
    return render(request, 'recipient_notification.html')

def recipienturgent(request):
    if request.method == 'POST':
        name = request.POST['name']
        blood = request.POST['bloodgroup']
        phone = request.POST['phone']
        location = request.POST['location']
        blooddetails = Urgent(name=name,blood=blood,phone=phone,location=location)
        blooddetails.save()
    return render(request, 'recipient_urgent_blood.html')

def urgentblood(request):
    urgentdetails = Urgent.objects.all()
    return render(request, 'urgentblood.html', {'urgent': urgentdetails})

def kvk_aplus(request):
    return render(request, 'kvk_a+.html')

def kvk_aminus(request):
    return render(request, 'kvk_a-.html')

def kvk_bplus(request):
    return render(request, 'kvk_b+.html')

def kvk_bminus(request):
    return render(request, 'kvk_b-.html')

def kvk_oplus(request):
    return render(request, 'kvk_o+.html')

def kvk_ominus(request):
    return render(request, 'kvk_o-.html')

def kvk_abplus(request):
    return render(request, 'kvk_ab+.html')

def kvk_abminus(request):
    return render(request, 'kvk_ab-.html')

def manjeri_aplus(request):
    return render(request, 'manjeri_a+.html')

def manjeri_aminus(request):
    return render(request, 'manjeri_a-.html')

def manjeri_bplus(request):
    return render(request, 'manjeri_b+.html')

def manjeri_bminus(request):
    return render(request, 'manjeri_b-.html')

def manjeri_oplus(request):
    return render(request, 'manjeri_o+.html')

def manjeri_ominus(request):
    return render(request, 'manjeri_o-.html')

def manjeri_abplus(request):
    return render(request, 'manjeri_ab+.html')

def manjeri_abminus(request):
    return render(request, 'manjeri_ab-.html')

