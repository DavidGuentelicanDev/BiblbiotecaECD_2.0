from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_sesion_page, name='login') #login del adminecd
]