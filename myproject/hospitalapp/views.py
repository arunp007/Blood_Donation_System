from django.shortcuts import render

def hospital(request):
    return render(request,'hospitalapp.html')

def hospitalsearch(request):
    return render(request, 'hospital_search.html')
