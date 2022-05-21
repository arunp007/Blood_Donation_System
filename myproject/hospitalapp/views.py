from django.shortcuts import render
from.models import Blood

def hospital(request):
    return render(request,'hospitalapp.html')

def hospitalsearch(request):
    return render(request, 'hospital_search.html')

def hospitalbloodrequest(request):
    if request.method == 'POST':
        blood = request.POST['blood']
        name = request.POST['name']
        phone = request.POST['phone']
        location = request.POST['location']
        details = Blood(blood=blood,name=name,phone=phone,location=location)
        details.save()
    return render(request, 'hospital_bloodrequest.html')

def hospitalnotification(request):
    infodetails = Blood.objects.all()
    return render(request, 'hospital_notification.html',{'info': infodetails})

def hospitalcamp(request):
    return render(request, 'hospital_camp.html')

def hospitalurgent(request):
    return render(request, 'hospital_urgent_blood.html')