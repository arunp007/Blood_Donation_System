from django.shortcuts import render

def main(request):
    return render(request, 'mainhome.html')

def about(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contactus.html')
