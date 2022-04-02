from django.urls import path
from.import views

urlpatterns = [

    path('donorlogin',views.donorlogin),
    path('hospitallogin',views.hospitallogin),
    path('recipientlogin',views.recipientlogin),
    path('admin',views.admin)
]