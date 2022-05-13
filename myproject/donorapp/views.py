from django.shortcuts import render
from.models import Blood

def donor(request):
    return render(request,'donorpage.html')

def donorsearch(request):
    return render(request, 'donor_search.html')

def donornotification(request):
    infodetails = Blood.objects.all()
    return render(request, 'donor_notification.html',{'info': infodetails})

def donorbloodrequest(request):
    if request.method == 'POST':
        blood = request.POST['blood']
        name  = request.POST['name']
        phone = request.POST['phone']
        location = request.POST['location']
        details = Blood(blood=blood,name=name,phone=phone,location=location)
        details.save()
    return render(request, 'donor_bloodrequest.html')



