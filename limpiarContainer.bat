rm -r tienda/migrations
docker-compose down -v
docker-compose up -d
python.exe ./manage.py makemigrations tienda
python.exe ./manage.py migrate

.\venv\Scripts\activate
pip install django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
pip install django-filters
python.exe -m pip install --upgrade pip
python.exe .\manage.py runserver

Activate ps1

docker-compose build

hacer el install requirement y el pip install django
incluir archivos que faltan de la tienda, añadir venv
en el venv añadir variables en ps1, crear contenedor, arrancar contenedor en segundo plano,
hacer migrate, arrancar app



pip install drf-spectacular
instalar apps, rest_framework, y spectacular settings
pip install drf-spectacular[sidecar]
instalar apps, y spectacular settings
./manage.py spectacular --color --file schema.yml
docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui
http://127.0.0.1/
