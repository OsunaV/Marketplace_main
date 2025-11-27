#                                     Documentacion completa(Desde Primer Parcial al Tercer Parcial)(27/11/25)

# Índice

- [Introducción](#introducción)
- [Explicación de comando](#explicación-de-comando)
- [Diagrama MVT](#diagrama-mvt)
- [Explicación de archivos y comandos](#explicación-de-archivos-y-comandos)
  - [settings.py](#settingspy)
  - [urls.py](#urlspy)
  - [models.py](#modelspy)
  - [views.py](#viewspy)
  - [Carpeta templates/store](#carpeta-templatesstore)
- [Ejecución del proyecto](#ejecución-del-proyecto)
- [Actualizaciones Del Tercer Parcial](#actualizaciones-del-tercer-parcial)
  - [Forms.py](#formspy-loginform-signupform-newitemform)
  - [Views.py](#viewspy-login-logout_user-detail-add_item)
  - [Templates store](#storetemplates-itemhtml-loginhtml-signuphtml-navigationhtml-formhtml)
- [Conclusión](#conclusión)

---

# Introducción

**Django** es un framework de desarrollo web de código abierto escrito en **Python**, diseñado para facilitar la creación de aplicaciones web rápidas y eficientes.  
Una de las principales razones para utilizar Django es su enfoque en el desarrollo rápido, ya que sigue el principio de **"baterías incluidas"**, proporcionando herramientas listas para usar, como autenticación de usuarios, formularios y seguridad. Esto permite a los desarrolladores centrarse en la lógica de negocio sin perder tiempo reinventando soluciones.  

Además, Django es **altamente escalable** y ofrece un rendimiento excelente, ideal para aplicaciones que crecen con el tiempo, como *Instagram* o *Pinterest*.  
En términos de **seguridad**, Django incluye protecciones integradas contra amenazas comunes como **SQL injection**, **XSS**, **CSRF** y **clickjacking**, ayudando a crear aplicaciones más seguras desde el principio.  

El framework tiene una **comunidad activa** y **documentación extensa**, facilitando el aprendizaje y resolución de problemas.  
Su sistema de **Object-Relational Mapping (ORM)** permite interactuar con bases de datos usando objetos Python en lugar de SQL.  
Django también ofrece una **interfaz administrativa preconfigurada** para gestionar los datos durante el desarrollo.  
Con su patrón **Model-Template-View (MTV)**, Django organiza el código de forma modular, promoviendo buenas prácticas y mantenimiento a largo plazo.

---

# Explicación de comando

```text
1) venv\Scripts\activate  
   Activa el entorno virtual en Windows.

2) pip install django  
   Instala Django en el entorno virtual.

3) django-admin startproject marketplace_main.  
   Crea un proyecto Django llamado marketplace_main.

4) python -m venv venv  
   Crea un entorno virtual llamado venv.

5) pip list  
   Lista los paquetes instalados en el entorno virtual.

6) dir  
   Lista archivos y carpetas en Windows.

7) python manage.py runserver  
   Inicia el servidor de desarrollo Django.

8) code .  
   Abre el proyecto en Visual Studio Code.

9) python manage.py createsuperuser  
   Crea un superusuario para la aplicación.

10) python manage.py migrate  
   Aplica migraciones a la base de datos.

11) python manage.py startapp store  
   Crea una aplicación llamada store dentro del proyecto.

12) python manage.py makemigrations  
   Genera migraciones según cambios en los modelos.

13) python manage.py migrate  
   Aplica las migraciones generadas.
Diagrama MVT
text
Copiar código
1. Cliente envía Request
2. Django recibe la solicitud
3. Router URL (urls.py) mapea la solicitud a la vista
4. View decide qué datos necesita y qué Template usar
   - Opción 1: Interactúa con el Model
   - Opción 2: Pasa directamente al Template
5. Model interactúa con la Base de Datos
6. Base de Datos devuelve datos al Model
7. Template genera la página web
8. Respuesta al Cliente: se envía la página completa
Explicación de archivos y comandos
settings.py
Centraliza la configuración del proyecto: base de datos, seguridad, middleware, autenticación, sesiones, personalización y escalabilidad.

python
Copiar código
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-7__w^=9l$(&lv=t4lse(s64__!fe0+gxyi&23^$w2ido6-%no2'

DEBUG = True
ALLOWED_HOSTS = []

LOGIN_URL = '/store/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'marketplace_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'marketplace_main.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
urls.py
Gestiona las rutas y mapea URLs a vistas específicas.

python
Copiar código
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
models.py
Define modelos que representan tablas de la base de datos mediante ORM.

python
Copiar código
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
views.py
Controla la lógica y flujo de la aplicación.

python
Copiar código
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Item, Category
from .forms import SignupForm, NewItemForm

def home(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    context = {'items': items, 'categories': categories}
    return render(request, 'store/home.html', context)

def contact(request):
    context = {'msg': 'Quieres otros productos?'}
    return render(request, 'store/contact.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {'item': item, 'related_items': related_items}
    return render(request, 'store/item.html', context)

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'store/signup.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def add_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('detail', pk=item.id)
    else:
        form = NewItemForm()
    context = {'form': form, 'title': 'New Item'}
    return render(request, 'store/form.html', context)
Carpeta templates/store
Contiene todas las páginas HTML:

base.html

contact.html

home.html

item.html

navigation.html

login.html

signup.html

form.html

login.html y signup.html:

html
Copiar código
{% extends 'store/base.html' %}
{% block title %}Login | {% endblock %}
{% block content %}
<div class="row p-4 d-flex justify-content-center align-items-center">
    <div class="shadow col-6 bg-white p-4 rounded-3">
        <h4 class="mb-6 text-center">Login</h4>
        <hr>
        <form action="." method="POST">
            {% csrf_token %}
            <div class="mb-3">
                <label class="form-label">Username:</label>
                {{form.username}}
            </div>
            <div class="mb-3">
                <label class="form-label">Password:</label>
                {{form.password}}
            </div>
            {% if form.errors or form.non_field_errors %}
                <div class="mb-4 p-6 bg-danger rounded">
                    {% for field in form %}
                        <h5 class="text-white">{{ field.errors }}</h5>
                    {% endfor %}
                    {{ form.non_field_errors }}
                </div>
            {% endif %}
            <div class="d-flex justify-content-center align-items-center">
                <button class="btn btn-primary mb-6">Login</button>
            </div>
            <div class="d-flex justify-content-center align-items-center">
                <a href="{% url 'register' %}">¿No tienes una cuenta? Creala aquí</a>
            </div>
        </form>
    </div>
</div>
{% endblock %}
html
Copiar código
{% extends 'store/base.html' %}
{% block title %}Registro | {% endblock %}
{% block content %}
<div class="row p-4 d-flex justify-content-center align-items-center">
    <div class="shadow col-6 bg-white p-4 rounded-3">
        <h4 class="mb-6 text-center">Registro</h4>
        <hr>
        <form action="." method="POST">
            {% csrf_token %}
            <div class="mb-3">
                <label class="form-label">Username:</label>
                {{form.username}}
            </div>
            <div class="mb-3">
                <label class="form-label">Email:</label>
                {{form.email}}
            </div>
            <div class="mb-3">
                <label class="form-label">Password:</label>
                {{form.password1}}
            </div>
            <div class="mb-3">
                <label class="form-label">Repite Password:</label>
                {{form.password2}}
            </div>
            {% if form.errors or form.non_field_errors %}
                <div class="mb-4 p-6 bg-danger rounded">
                    {% for field in form %}
                        <h5 class="text-white">{{ field.errors }}</h5>
                    {% endfor %}
                    {{ form.non_field_errors }}
                </div>
            {% endif %}
            <div class="d-flex justify-content-center align-items-center">
                <button class="btn btn-primary mb-6">Registro</button>
            </div>
            <div class="d-flex justify-content-center align-items-center">
                <a href="{% url 'login' %}">¿Ya tienes una cuenta? Accede aquí</a>
            </div>
        </form>
    </div>
</div>
{% endblock %}
Ejecución del proyecto
Visualización de items en la página web.

Sección de contacto.

Uso de Django Admin para crear tablas y gestionar datos.

Actualizaciones Del Tercer Parcial
Forms.py
python
Copiar código
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Item

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tu usuario','class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tu Usuario','class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Tu Email','class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repite Password','class': 'form-control'}))
Views.py
python
Copiar código
# Ya se mostró en la sección anterior (add_item, login, logout, register, detail)
Conclusión
El proyecto implementa:

Forms.py: Formularios personalizados y validación.

Views.py: Registro, login, detalle de productos y protección de vistas con @login_required.

Urls.py: Rutas bien definidas y uso de LoginView.

Templates: Diseño consistente usando base.html.

Corrección: Se ajustó la visualización de errores en los formularios para mejorar la experiencia del usuario.

