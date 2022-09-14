from django.shortcuts import render
from.models import *

def main(request):
    return render(request, 'mainhome.html')

def about(request):
    return render(request, 'aboutus.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['emailid']
        message = request.POST['message']
        contact_data = Contact(name = name, email = email, message = message)
        contact_data.save()
    return render(request, 'contactus.html')

def contact_data(request):
    contact_details = Contact.objects.all()
    return render(request, 'contact_details.html', {'contact': contact_details})


