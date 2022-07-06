from django.urls import path
from.import views

urlpatterns = [
    path('donor_signup', views.donor_signup, name = 'donor_signup'),
    path('donor_info', views.donor_info, name = 'donor_info'),
    path('donors', views.donors, name = 'donors'),
    path('donor_update/<int:id>', views.donors_update, name = 'donor_update'),
    path('donor_delete/<int:id>', views.donors_delete, name = 'donor_delete'),
    path('recipient_signup', views.recipient_signup, name = 'recipient_signup'),
    path('recipients', views.recipients, name = 'recipients'),
    path('recipient_update/<int:id>', views.recipients_update, name = 'recipient_update'),
    path('recipient_delete/<int:id>', views.recipients_delete, name = 'recipient_delete'),
    path('hospital_signup', views.hospital_signup, name = 'hospital_signup'),
    path('hospitals', views.hospitals, name = 'hospitals'),
    path('hospital_update/<int:id>', views.hospitals_update, name = 'hospital_update'),
    path('hospital_delete/<int:id>', views.hospitals_delete, name = 'hospital_delete'),
    path('donorlogin', views.donorlogin, name = 'donorlogin'),
    path('hospitallogin', views.hospitallogin, name = 'hospitallogin'),
    path('recipientlogin', views.recipientlogin, name = 'recipientlogin'),
    path('admin', views.admin, name = "adminlogin"),
    path('admin_logout', views.admin_logout, name = 'admin_logout')
]