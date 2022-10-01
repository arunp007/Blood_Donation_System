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
    path('kvk_aplus', views.kvk_aplus),
    path('kvk_aminus', views.kvk_aminus),
    path('kvk_bplus', views.kvk_bplus),
    path('kvk_bminus', views.kvk_bminus),
    path('kvk_oplus', views.kvk_oplus),
    path('kvk_ominus', views.kvk_ominus),
    path('kvk_abplus', views.kvk_abplus),
    path('kvk_abminus', views.kvk_abminus),
    path('manjeri_aplus', views.manjeri_aplus),
    path('manjeri_aminus', views.manjeri_aminus),
    path('manjeri_bplus', views.manjeri_bplus),
    path('manjeri_bminus', views.manjeri_bminus),
    path('manjeri_oplus', views.manjeri_oplus),
    path('manjeri_ominus', views.manjeri_ominus),
    path('manjeri_abplus', views.manjeri_abplus),
    path('manjeri_abminus', views.manjeri_abminus),
  
]