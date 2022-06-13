from django.urls import path
from.import views

urlpatterns = [
    path('donor', views.donor, name = 'donorsignup'),
    path('recipient', views.recipient, name = 'recipientsignup'),
    path('hospital', views.hospital, name = 'hospitalsignup')
]