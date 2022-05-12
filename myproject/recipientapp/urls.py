from django.urls import path
from.import views

urlpatterns = [
    path('recipient',views.recipient,name="recipient_home"),
    path('recipientsearch',views.recipientsearch,name="recipient_search"),
    path('bloodrequest',views.bloodrequest,name="blood_request")
]