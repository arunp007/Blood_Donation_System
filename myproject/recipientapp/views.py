from django.shortcuts import render

def recipient(request):
    return render(request,'recipientpage.html')

def search(request):
    return render(request,'search.html')

