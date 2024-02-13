# permissions.py: Define una clase de permisos personalizada (VehiculoPermission) que
# controla quién puede realizar acciones en los vehículos. En este caso, permite a los
# usuarios autenticados realizar cualquier acción, pero niega el acceso a los usuarios no autenticados.



from rest_framework import permissions
from rest_framework.permissions import BasePermission


class VehiculoPermission(BasePermission):
    message = "No tienes acceso."

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user.is_authenticated:
                return True
            else:
                return False
