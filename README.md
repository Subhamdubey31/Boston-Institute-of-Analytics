# Boston-Institute-of-Analytics
Hello 
I have added all the necessary files in the repository.

************Task 1: Framework Setup************
1. Django: Create a new Django project.
Flask: Set up a new Flask project.
2. Implement a simple route or view that returns a "Hello, Django!" or "Hello, Flask!" message.
   
Step 1: Install Django
If you haven't already installed Django, you can install it using:

pip install Django
Step 2: Create a New Django Project
Use the following command to create a new Django project:


django-admin startproject myproject
This will create a new directory named myproject with the necessary project files.

Step 3: Create a Django App
cd task1
python manage.py startapp boston1
Inside your project, you can create a new app:

Step 4: Run the Development Server
Start the Django development server using:
python manage.py runserver



****************Task 2: RESTful API Development****************
1. Django: Implement a minimal Django REST framework API for managing a collection of items (e.g., books, movies).
Flask: Implement a minimal Flask RESTful API for managing a collection of items.
2. Include endpoints for retrieving all items and adding a new item.

Step 1: Create a New Django Project
django-admin startproject Task2

Step 2: Create a New Django App
cd Task2
python manage.py startapp boston2
Step 3: Run Migrations
Run migrations to apply changes to your database:
python manage.py makemigrations
python manage.py migrate

Step 4: Run the Development Server
python manage.py runserver
Visit the provided URL and use tools like Postman to test your API endpoints.

Step 5: Test Endpoints
Retrieve all items (GET request): http://127.0.0.1:8000/boston2/books/


************Task 3: Database Interaction************
1. Django: Use Django models for database interaction with the API.

Step 1. Create Django Project:
Use the following command to create a new Django project named myproject:
django-admin startproject task3

Step 2. Install Django REST Framework:
Install Django REST Framework using pip with the following command:
pip install djangorestframework

Step 3. Create Django App:
Create a Django app named items within the project using:
python manage.py startapp boston3

Step 4. Run Migrations:
Apply the model changes to the database by running:
python manage.py makemigrations
python manage.py migrate

Step 5. Run Development Server:
Run the development server with:
python manage.py runserver
Access the API endpoints (e.g., http://127.0.0.1:8000/boston3/books/).

Step 6. Data entry through URl
Fill all the required filled on the URL.

Step 7. Verifying of the data.
Checking whether the data has been successfully reflecting inside the database through terminal.
python3 manage.py Shell


********Task 4: Authentication (Optional)********
1. Django: Implement token-based authentication using Django REST framework.
Flask: Implement token-based authentication using Flask-JWT-Extended.

Install Django REST Framework and the Token package using pip:
pip install djangorestframework
pip install djangorestframework-authtoken

2. Configure Django REST Framework in Settings:
Open the settings.py file in your Django project and add the following configurations:
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
]

3. Run Migrations:
Apply the migrations to create the necessary database tables for authentication:
python manage.py makemigrations
python manage.py migrate

4. Create Token for Users:
For existing users, generate tokens using the Django shell:
python manage.py shell

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
user = User.objects.get(username='your_username')
Token.objects.create(user=user)

6. Testing with Postman:
Use Postman to make requests to the authenticated endpoints by including the token in the Authorization header.

URL:- http://127.0.0.1:8000/task/api-token-auth/

Task 5. Added within the task 4.

********Note:- Task 4 and Task 5 is inside the file Backend project.********

