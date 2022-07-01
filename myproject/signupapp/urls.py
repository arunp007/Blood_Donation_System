from django.urls import path
from.import views

urlpatterns = [
    path('donor', views.donor, name = 'donorsignup'),
    path('donor_details', views.donor_details, name = 'donor_details'),
    path('donor_data', views.donor_data, name = 'donor_data'),
    path('recipient', views.recipient, name = 'recipientsignup'),
    path('hospital', views.hospital, name = 'hospitalsignup')
]