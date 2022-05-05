from django.urls import path
from.import views

urlpatterns = [

    path('donor',views.donor, name = "donor"),
    path('recipient',views.recipient, name = "recipient"),
    path('hospital',views.hospital, name = "hospital")
]