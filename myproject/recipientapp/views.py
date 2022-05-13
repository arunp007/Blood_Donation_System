from django.shortcuts import render
from.models import Blood

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

def recipient_notification(request):
    infodetails = Blood.objects.all()
    return render(request, 'recipient_notification.html',{'info': infodetails})


