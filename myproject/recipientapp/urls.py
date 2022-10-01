from django.urls import path
from.import views

urlpatterns = [
    path('recipient',views.recipient,name="recipient_home"),
    path('recipientsearch',views.recipientsearch,name="recipient_search"),
    path('recipientbloodrequest',views.recipientbloodrequest,name="recipient_bloodrequest"),
    path('recipient_notification',views.recipient_notification,name="recipient_notification"),
    path('recipienturgent',views.recipienturgent,name='recipienturgent'),
    path('bloodrequest',views.bloodrequest, name="bloodrequest"),
    path('urgentblood',views.urgentblood, name="urgentblood"),
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