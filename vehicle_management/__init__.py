# 1. Gestión de Vehículos
#
# Crea una API REST con Django para la gestión de una base de datos de Vehículos.
#
# Se debe guardar la siguiente información de cada Vehículo.
# Tipo vehículo (Coche, Ciclomotor o Motocicleta).
# Chasis. Número identificativo único del Vehículo.
# Marca. (Las marcas son un campo que depende de un listado ampliable).
# Modelo. (Cadena de texto simple)
# Matrícula. (Cadena identificativa única del vehículo)
# Color. (Debe poder elegirse de un conjunto predefinido)
# Fecha de fabricación. Obligatorio
# Fecha Matriculación. Fecha de alta de la matrícula.
# Fecha de Baja. Fecha de baja de la matrícula
# Suspendido. Flag que indica si el vehículo se encuentra en baja temporal.
#
# Requisitos del Ejercicio.
# Define los modelos correctamente
# Publica servicios para la gestión (CRUD) de las marcas
# Publica servicios para la gestión (CRUD) de los vehículos.
# Publica un servicio para el listado de los vehículos de una marca determinada.
# Restringe las operaciones de creación, actualización y borrado sólo a usuarios autenticados.
# Permite que la API visualice la información en HTML por defecto de Django REST Framework y que se puedan navegar por las relaciones del modelo con Hyperenlaces.
# Expón la API con openapi y swagger
#
# Propuestas de ampliación:
# Crea servicios que permitan obtener los listados ordenados por fecha.
# Crea un servicio que permita filtrar vehículos por Marcas, modelos y colores.
# Diferencia en la aplicación entre usuarios editores y resto de usuarios. Solo los usuarios editores podrán realizar operaciones que supongan creación, actualización o eliminación de datos.
