from django.urls import path
from.import views

urlpatterns = [
    path('admin/',views.admin, name='admin_home'),
    path('adminnotification/',views.adminnotification, name='admin_notification')
]