from django.urls import path
from.import views

urlpatterns = [
    path('donor', views.donor, name = 'donorsignup'),
    path('donor_details', views.donor_details, name = 'donor_details'),
    path('donor_update/<int:id>', views.donor_update, name = 'donor_update'),
    path('donor_delete/<int:id>', views.donor_delete, name = 'donor_delete'),
    path('donor_data', views.donor_data, name = 'donor_data'),
    path('recipient', views.recipient, name = 'recipientsignup'),
    path('recipient_details',views.recipient_details, name = 'recipient_details'),
    path('recipient_update<int:id>', views.recipient_update, name = 'recipient_update'),
    path('recipient_delete<int:id>', views.recipient_delete, name = 'recipient_delete'),
    path('hospital', views.hospital, name = 'hospitalsignup'),
    path('hospital_details', views.hospital_details, name = 'hospital_details'),
    path('hospital_update/<int:id>', views.hospital_update, name = 'hospital_update'),
    path('hospital_delete/<int:id>', views.hospital_delete, name = 'hospital_delete'),
]