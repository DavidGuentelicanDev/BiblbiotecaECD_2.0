from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required, user_passes_test


#Login, Permisos y Logout

#pagina login
def inicio_sesion_page(request):
    if request.user.is_authenticated:
        return redirect('principal')
    return render(request, 'ecd_admin_app/login.html')

#login
@csrf_exempt
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

#logout
def adm_logout(request):
    logout(request)
    return JsonResponse({"status": "success"})

#permisos todo el staff
def staff_requerido(user):
    return user.is_staff

#permisos solo bibliotecario y admin
def bibliotecario_requerido(user):
    return user.rol in [1, 2]

#permisos solo admin
def administrador_requerido(user):
    return user.rol == 1

######################################################################################################################################

#Home

#pagina principal
@login_required
@user_passes_test(staff_requerido)
def home(request):
    return render(request, 'ecd_admin_app/home.html')
