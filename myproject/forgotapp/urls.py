from django.urls import path
from.import views

urlpatterns = [

    path('forgot',views.forgot),
    path('reset',views.reset)
]