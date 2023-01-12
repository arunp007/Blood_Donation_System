from django.urls import path
from.import views

urlpatterns = [
    path('admin/',views.admin, name='admin_home'),
    path('admin_notification/',views.admin_notification, name='admin_notification'),
    path('donor_notification', views.donor_notification, name = 'donor_notification'),
    path('recipient_notification', views.recipient_notification, name = 'recipient_notification'),
    path('hospital_notification', views.hospital_notification, name = 'hospital_notification'),
    path('notification', views.notification, name = 'notification'),
]