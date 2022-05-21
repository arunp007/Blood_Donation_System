from django.urls import path
from.import views

urlpatterns = [
    path('hospital',views.hospital,name="hospital_home"),
    path('hospitalsearch',views.hospitalsearch,name="hospital_search"),
    path('hospitalbloodrequest',views.hospitalbloodrequest,name="hospitalbloodrequest"),
    path('hospitalnotification',views.hospitalnotification,name="hospitalnotification"),
    path('hospitalcamp',views.hospitalcamp,name='hospitalcamp'),
    path('hospitalurgent',views.hospitalurgent,name='hospitalurgent')
  
]