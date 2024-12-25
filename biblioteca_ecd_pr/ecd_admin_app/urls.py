from django.urls import path
from . import views

urlpatterns = [
    #login, permisos y logout
    path('', views.inicio_sesion_page, name='login_page'), #login del adminecd
    path('adm_login/', views.adm_login, name='login'), #ruta para login
    path('adm_logout/', views.adm_logout, name='logout'), #ruta de logout
    path('sin_permisos/', views.sin_permisos, name='sin_acceso'), #pagina sin permisos
    #home y perfil
    path('home/', views.home, name='principal'), #ruta pagina principal
]
