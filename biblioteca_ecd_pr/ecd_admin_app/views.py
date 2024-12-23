from django.shortcuts import render
from core_app.models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


#Login

#pagina login
def inicio_sesion_page(request):
    return render(request, 'ecd_admin_app/login.html')

#login
def adm_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) #leer json del cuerpo de la solicitud http
            username = data.get("usuarioLogin")
            password = data.get("contrasenaLogin")
            #autentificar usando username y password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return JsonResponse({"status": "success"})
                else:
                    return JsonResponse({"status": "error", "message": "No tienes permisos para acceder"})
            else:
                return JsonResponse({"status": "error", "message": "Credenciales inválidas"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Error procesando la solicitud: {str(e)}"})
    else:
        return JsonResponse({"status": "error", "message": "Método no permitido"}, status=405)

######################################################################################################################################

#Home

#pagina principal
def home(request):
    return render(request, 'ecd_admin_app/home.html')
