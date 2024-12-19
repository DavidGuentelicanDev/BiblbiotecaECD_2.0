from django.shortcuts import render
from core_app.models import Usuario


#Login

#pagina login
def inicio_sesion_page(request):
    return render(request, 'ecd_admin_app/login.html')
