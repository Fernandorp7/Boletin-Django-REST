# urls.py: Define las URL para acceder a las vistas de la API. Utiliza un enrutador
# (DefaultRouter) para generar automáticamente las URL para los ViewSets registrados.




from django.urls import include, path
from rest_framework import routers

from vehicle_management import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'vehiculos', views.VehiculoViewSet)
router.register(r'marcas', views.MarcaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls