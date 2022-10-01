from django.shortcuts import render

def donor(request):
    return render(request,'donorpage.html')

def donorsearch(request):
    return render(request, 'donor_search.html')

def donornotification(request):
    return render(request, 'donor_notification.html')

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

















