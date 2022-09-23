from django.shortcuts import render

def donor(request):
    return render(request,'donorpage.html')

def donorsearch(request):
    return render(request, 'donor_search.html')

def donornotification(request):
    return render(request, 'donor_notification.html')

def kvk_donors_table(request):
    return render(request, 'kvk_donor.html')










