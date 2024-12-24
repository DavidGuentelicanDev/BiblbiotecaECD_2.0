from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_sesion_page, name='login'), #login del adminecd
    path('adm_login/', views.adm_login, name='login_adm'), #ruta para login
    path('home/', views.home, name='principal'), #ruta pagina principal
]
