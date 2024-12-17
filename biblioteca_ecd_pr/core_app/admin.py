from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Editorial, Libro, Autor, AutorPorLibro, Usuario, Reserva


# Clase de usuario para personalizar el Usuario del Admin Django
class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'rut', 'telefono', 'rol')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'rut', 'telefono', 'rol'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


# Incluir en el Admin de Django
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(AutorPorLibro)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Reserva)
