from django.urls import path
from.import views

urlpatterns = [
    path('recipient',views.recipient),
    path('search',views.search, name = "search")
]