from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_sesion_page, name='login_page'), #login del adminecd
    path('adm_login/', views.adm_login, name='login'), #ruta para login
    path('home/', views.home, name='principal'), #ruta pagina principal
    path('adm_logout/', views.adm_logout, name='logout'), #ruta de logout
]
