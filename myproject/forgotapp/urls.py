from django.urls import path
from.import views

urlpatterns = [

    path('forgot',views.forgot,name="forgot"),
    path('reset',views.reset)
]