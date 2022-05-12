from django.urls import path
from.import views

urlpatterns = [
    path('hospital',views.hospital,name="hospital_home"),
    path('hospitalsearch',views.hospitalsearch,name="hospital_search")
]