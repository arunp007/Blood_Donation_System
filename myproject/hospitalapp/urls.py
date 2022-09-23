from django.urls import path
from.import views

urlpatterns = [
    path('hospital', views.hospital, name="hospital_home"),
    path('hospitalsearch', views.hospitalsearch, name="hospital_search"),
    path('hospitalnotification', views.hospitalnotification, name="hospitalnotification"),
    path('hospitalcamp', views.hospitalcamp, name='hospitalcamp'),
    path('camptable', views.camptable, name="camptable"),
    path('camp_details', views.camp_details, name = 'camp_details'),
    path('camp', views.camp, name = 'camp'),
    path('camp_update<int:id>', views.camp_update, name = 'camp_update'),
    path('camp_delete<int:id>', views.camp_delete, name = 'camp_delete'),
    path('donors_details', views.kvk_hospital_table),
  
]