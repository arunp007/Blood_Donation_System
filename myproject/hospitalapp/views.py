from django.shortcuts import render, redirect
from.models import *

def hospital(request):
    return render(request,'hospitalapp.html')

def hospitalsearch(request):
    return render(request, 'hospital_search.html')

def hospitalcamp(request):
    if request.method == 'POST':
        camp = request.POST['camp']
        date = request.POST['date']
        address = request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        details = Camps(camp = camp, date = date, address = address, state = state, district = district, name = name, phone = phone, email = email)
        details.save()
    return render(request, 'hospital_camp.html')

def camptable(request):
    camp_details = Camps.objects.all()
    return render(request, 'camptable.html', {'details' : camp_details})

def camp_details(request):
    camp_data = Camps.objects.all()
    return render(request, 'camp_details.html', {'camp': camp_data})

def camp(request):
    if request.method == 'POST':
        camp = request.POST['camp']
        date = request.POST['date']
        address = request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        details = Camps(camp = camp, date = date, address = address, state = state, district = district, name = name, phone = phone, email = email)
        details.save()
    return render(request, 'camp.html')

def camp_update(request,id):
    if request.method == 'POST':
        update_data = ""
        camp = request.POST['camp']
        date = request.POST['date']
        address = request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        Camps.objects.filter(id = id).update(camp = camp, date = date, address = address, state = state, district = district, name = name, phone = phone, email = email)
        return redirect('camp_details')

    else:
        update_data = Camps.objects.get(id = id)
        return render(request, 'camp.html', {'update': update_data})

def camp_delete(request,id):
    Camps.objects.get(id = id).delete()
    return redirect('camp_details')

def kvk_aplus(request):
    return render(request, 'hospital_search/kvk_a+.html')

def kvk_aminus(request):
    return render(request, 'hospital_search/kvk_a-.html')

def kvk_bplus(request):
    return render(request, 'hospital_search/kvk_b+.html')

def kvk_bminus(request):
    return render(request, 'hospital_search/kvk_b-.html')

def kvk_oplus(request):
    return render(request, 'hospital_search/kvk_o+.html')

def kvk_ominus(request):
    return render(request, 'hospital_search/kvk_o-.html')

def kvk_abplus(request):
    return render(request, 'hospital_search/kvk_ab+.html')

def kvk_abminus(request):
    return render(request, 'hospital_search/kvk_ab-.html')

def manjeri_aplus(request):
    return render(request, 'hospital_search/manjeri_a+.html')

def manjeri_aminus(request):
    return render(request, 'hospital_search/manjeri_a-.html')

def manjeri_bplus(request):
    return render(request, 'hospital_search/manjeri_b+.html')

def manjeri_bminus(request):
    return render(request, 'hospital_search/manjeri_b-.html')

def manjeri_oplus(request):
    return render(request, 'hospital_search/manjeri_o+.html')

def manjeri_ominus(request):
    return render(request, 'hospital_search/manjeri_o-.html')

def manjeri_abplus(request):
    return render(request, 'hospital_search/manjeri_ab+.html')

def manjeri_abminus(request):
    return render(request, 'hospital_search/manjeri_ab-.html')

def mal_aplus(request):
    return render(request, 'hospital_search/mal_a+.html')

def mal_aminus(request):
    return render(request, 'hospital_search/mal_a-.html')

def mal_bplus(request):
    return render(request, 'hospital_search/mal_b+.html')

def mal_bminus(request):
    return render(request, 'hospital_search/mal_b-.html')

def mal_oplus(request):
    return render(request, 'hospital_search/mal_o+.html')

def mal_ominus(request):
    return render(request, 'hospital_search/mal_o-.html')

def mal_abplus(request):
    return render(request, 'hospital_search/mal_ab+.html')

def mal_abminus(request):
    return render(request, 'hospital_search/mal_ab-.html')

def w_aplus(request):
    return render(request, 'hospital_search/wandoor_a+.html')

def w_aminus(request):
    return render(request, 'hospital_search/wandoor_a-.html')

def w_bplus(request):
    return render(request, 'hospital_search/wandoor_b+.html')

def w_bminus(request):
    return render(request, 'hospital_search/wandoor_b-.html')

def w_oplus(request):
    return render(request, 'hospital_search/wandoor_o+.html')

def w_ominus(request):
    return render(request, 'hospital_search/wandoor_o-.html')

def w_abplus(request):
    return render(request, 'hospital_search/wandoor_ab+.html')

def w_abminus(request):
    return render(request, 'hospital_search/wandoor_ab-.html')

def n_aplus(request):
    return render(request, 'hospital_search/nlbr_a+.html')

def n_aminus(request):
    return render(request, 'hospital_search/nlbr_a-.html')

def n_bplus(request):
    return render(request, 'hospital_search/nlbr_b+.html')

def n_bminus(request):
    return render(request, 'hospital_search/nlbr_b-.html')

def n_oplus(request):
    return render(request, 'hospital_search/nlbr_o+.html')

def n_ominus(request):
    return render(request, 'hospital_search/nlbr_o-.html')

def n_abplus(request):
    return render(request, 'hospital_search/nlbr_ab+.html')

def n_abminus(request):
    return render(request, 'hospital_search/nlbr_ab-.html')

def v_aplus(request):
    return render(request, 'hospital_search/v_a+.html')

def v_aminus(request):
    return render(request, 'hospital_search/v_a-.html')

def v_bplus(request):
    return render(request, 'hospital_search/v_b+.html')

def v_bminus(request):
    return render(request, 'hospital_search/v_b-.html')

def v_oplus(request):
    return render(request, 'hospital_search/v_o+.html')

def v_ominus(request):
    return render(request, 'hospital_search/v_o-.html')

def v_abplus(request):
    return render(request, 'hospital_search/v_ab+.html')

def v_abminus(request):
    return render(request, 'hospital_search/v_ab-.html')
