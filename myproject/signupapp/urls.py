from django.urls import path
from.import views

urlpatterns = [

    path('donor',views.donor),
    path('recipient',views.recipient),
    path('hospital',views.hospital)
]