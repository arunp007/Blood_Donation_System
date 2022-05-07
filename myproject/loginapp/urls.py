from django.urls import path
from.import views

urlpatterns = [

    path('donorlogin',views.donorlogin, name = "donorlogin"),
    path('hospitallogin',views.hospitallogin, name = "hospitallogin"),
    path('recipientlogin',views.recipientlogin, name = "recipientlogin"),
    path('admin',views.admin, name = "adminlogin")
]