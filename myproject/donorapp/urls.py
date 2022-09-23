from django.urls import path
from.import views

urlpatterns = [
    path('donor',views.donor,name="donor_home"),
    path('donorsearch',views.donorsearch,name="donor_search"),
    path('donornotification', views.donornotification,name="donornotification"),
    path('donors_details', views.kvk_donors_table),
]