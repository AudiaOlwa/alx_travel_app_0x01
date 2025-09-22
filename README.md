# alx_travel_app_0x00
# Seed & run
Django Travel App project with MySQL, DRF, Swagger, and CORS.

1. Installer dépendances:
   pip install -r requirements.txt
   pip install django djangorestframework

2. Activer env virtuel, puis:
   python manage.py makemigrations
   python manage.py migrate

3. (Optionnel) créer un superuser:
   python manage.py createsuperuser

4. Seeder les données:
   python manage.py seed

5. Lancer le serveur:
   python manage.py runserver

6. Ouvrir la browsable API:
   http://127.0.0.1:8000/api/listings/
