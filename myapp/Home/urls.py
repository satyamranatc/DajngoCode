
from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home, name="Home"),
    path('Data/',views.Data, name="Data"),

]
