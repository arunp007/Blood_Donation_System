from django.shortcuts import render

def forgot(request):
    return render(request,'forgotpass.html')

def reset(request):
    return render(request,'resetpass.html')
