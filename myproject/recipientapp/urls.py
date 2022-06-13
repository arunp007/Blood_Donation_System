from django.urls import path
from.import views

urlpatterns = [
    path('recipient',views.recipient,name="recipient_home"),
    path('recipientsearch',views.recipientsearch,name="recipient_search"),
    path('recipientbloodrequest',views.recipientbloodrequest,name="recipient_bloodrequest"),
    path('recipient_notification',views.recipient_notification,name="recipient_notification"),
    path('recipienturgent',views.recipienturgent,name='recipienturgent'),
    path('bloodrequest',views.bloodrequest, name="bloodrequest"),
    path('urgentblood',views.urgentblood, name="urgentblood")

]