#                                     Documentacion completa(Desde Primer Parcial al Tercer Parcial)(27/11/25)

# Índice de Documentación Django (27/11/25)
1. [Introducción](#introducción)
   - [Qué es Django](#qué-es-django)
   - [Ventajas de usar Django](#ventajas-de-usar-django)
   - [Seguridad en Django](#seguridad-en-django)
   - [Sistema ORM y administración](#sistema-orm-y-administración)
   - [Patrón MVT](#patrón-mvt)

2. [Explicación de comandos](#explicación-de-comandos)
   - [Activar entorno virtual](#activar-entorno-virtual-venvscriptsactivate)
   - [Instalar Django](#instalar-django-pip-install-django)
   - [Crear proyecto Django](#crear-proyecto-django-django-admin-startproject-marketplace_main)
   - [Crear entorno virtual](#crear-entorno-virtual-python-m-venv-venv)
   - [Ver paquetes instalados](#ver-paquetes-instalados-pip-list)
   - [Listar archivos](#listar-archivos-dir)
   - [Ejecutar servidor de desarrollo](#ejecutar-servidor-de-desarrollo-python-manage-py-runserver)
   - [Abrir VS Code](#abrir-vs-code-code-)
   - [Crear superusuario](#crear-superusuario-python-manage-py-createsuperuser)
   - [Aplicar migraciones](#aplicar-migraciones-python-manage-py-migrate)
   - [Crear aplicación](#crear-aplicación-python-manage-py-startapp-store)
   - [Generar migraciones](#generar-migraciones-python-manage-py-makemigrations)
   - [Aplicar migraciones](#aplicar-migraciones-python-manage-py-migrate-1)

3. [Diagrama MVT](#diagrama-mvt)
   - [Solicitud del cliente](#solicitud-del-cliente)
   - [Enrutamiento URL](#enrutamiento-url)
   - [Vistas (Views)](#vistas-views)
   - [Modelos (Models)](#modelos-models)
   - [Base de datos](#base-de-datos)
   - [Plantillas (Templates)](#plantillas-templates)
   - [Respuesta al cliente](#respuesta-al-cliente)

4. [Explicación de archivos y configuración](#explicación-de-archivos-y-configuración)
   - [`settings.py`](#settingspy)
   - [`urls.py`](#urlspy)
   - [`models.py`](#modelspy)
   - [`views.py`](#viewspy)
   - [`forms.py`](#formspy)
   - [`templates/store/`](#templatesstore)

5. [Ejecución del proyecto](#ejecución-del-proyecto)
   - [Visualización de items en la web](#visualización-de-items-en-la-web)
   - [Sección de contacto](#sección-de-contacto)
   - [Uso del panel de administración de Django](#uso-del-panel-de-administración-de-django)

6. [Actualizaciones del Tercer Parcial](#actualizaciones-del-tercer-parcial)
   - [Nuevos formularios (`forms.py`)](#nuevos-formularios-formspy)
   - [Funciones actualizadas en `views.py`](#funciones-actualizadas-en-viewspy)
   - [Decorador `@login_required`](#decorador-login_required)
   - [Rutas nuevas en `urls.py`](#rutas-nuevas-en-urlspy)
   - [Plantillas para login y registro](#plantillas-para-login-y-registro)

7. [Conclusión](#conclusión)
   - [Resumen de la implementación](#resumen-de-la-implementación)
   - [Observaciones sobre vistas, rutas, formularios y plantillas](#observaciones-sobre-vistas-rutas-formularios-y-plantillas)
   - [Recomendaciones de mejoras](#recomendaciones-de-mejoras)

# Introducción

**Django** es un framework de desarrollo web de código abierto escrito en **Python**, diseñado para facilitar la creación de aplicaciones web rápidas y eficientes.
Una de las principales razones para utilizar Django es su enfoque en el desarrollo rápido, ya que sigue el principio de **"baterías incluidas"**, proporcionando herramientas listas para usar, como autenticación de usuarios, formularios y seguridad. Esto permite a los desarrolladores centrarse en la lógica de negocio sin perder tiempo reinventando soluciones.
Además, Django es **altamente escalable** y ofrece un rendimiento excelente, lo que lo convierte en una opción ideal para aplicaciones que necesitan crecer con el tiempo, como lo demuestran empresas como *Instagram* y *Pinterest*.
En términos de **seguridad**, Django incluye protecciones integradas contra amenazas comunes como **SQL injection**, **XSS**, **CSRF** y **clickjacking**, lo que ayuda a crear aplicaciones más seguras desde el principio.
El framework también cuenta con una **comunidad activa** y una **documentación extensa**, lo que facilita el aprendizaje y la resolución de problemas.
Su sistema de **Object-Relational Mapping (ORM)** permite interactuar con bases de datos utilizando objetos Python en lugar de SQL, haciendo el código más limpio y fácil de mantener.
Además, Django ofrece una **interfaz administrativa preconfigurada**, que facilita la gestión de los datos de la aplicación durante el desarrollo.
Con su patrón de diseño **Model-Template-View (MTV)**, Django organiza el código de manera modular, promoviendo buenas prácticas de desarrollo y facilitando el mantenimiento a largo plazo.

# Explicación de comando
1)venv\Scripts\activate  
Este comando activa el entorno virtual de Python en sistemas Windows. El entorno virtual es un espacio aislado donde puedes instalar y gestionar paquetes de Python sin que afecten a otras aplicaciones o proyectos. Esto es útil para evitar conflictos de dependencias entre diferentes proyectos.

2)pip install django  
Este comando instala Django en el entorno virtual. Al ejecutarlo, se descarga e instala el framework Django y sus dependencias, lo que te permite comenzar a desarrollar aplicaciones web con Django en ese entorno específico.

3)django-admin startproject marketplace_main.  
Con este comando, se crea un nuevo proyecto de Django llamado marketplace_main. Este comando genera automáticamente una estructura de directorios con los archivos necesarios para empezar a trabajar en la aplicación web, como settings.py, urls.py, y wsgi.py.

4)python -m venv venv  
Este comando crea un nuevo entorno virtual llamado venv dentro del directorio actual. Un entorno virtual es una herramienta clave para manejar dependencias de manera aislada, permitiendo que cada proyecto tenga sus propias bibliotecas y versiones sin interferir con otros proyectos.

5)pip list  
Este comando muestra una lista de todos los paquetes instalados en el entorno virtual actual. Es útil para verificar qué bibliotecas y versiones tienes instaladas, permitiendo saber si Django o cualquier otra dependencia está correctamente instalada.

6)dir  
Este comando, que se utiliza en sistemas Windows, muestra una lista de archivos y carpetas dentro del directorio actual. Es útil para verificar la estructura de tu proyecto o para navegar por los archivos sin tener que abrir el explorador de archivos.

7)python manage.py runserver  
Este comando inicia el servidor de desarrollo de Django, lo que te permite ver tu aplicación web en un navegador local (normalmente en localhost:8000). Es esencial para probar y desarrollar la aplicación de manera interactiva.

8)code .  
Este comando abre el directorio actual en Visual Studio Code, si tienes este editor de código instalado. Es un atajo práctico para comenzar a trabajar en tu proyecto sin necesidad de buscarlo manualmente desde el editor.

9)python manage.py createsuperuser  
Este comando crea un superusuario (administrador) para tu aplicación Django. El superusuario te permite acceder al panel de administración de Django, donde podrás gestionar la base de datos, los usuarios y otros aspectos del proyecto de manera visual y fácil de usar.

10)python manage.py migrate  
El comando migrate aplica todas las migraciones pendientes a la base de datos. Las migraciones son un sistema de Django para gestionar cambios en los modelos, como agregar campos o crear nuevas tablas, y este comando asegura que la base de datos esté sincronizada con el código de los modelos.

11)python manage.py startapp store  
Este comando crea una nueva aplicación dentro del proyecto Django llamada store. En Django, una "aplicación" es un módulo que contiene funcionalidades específicas, como el manejo de productos o usuarios. Este comando genera la estructura básica de una aplicación para que puedas comenzar a desarrollar su funcionalidad.

12)python manage.py makemigrations  
Este comando genera las migraciones necesarias para reflejar los cambios realizados en los modelos de la aplicación. Si, por ejemplo, agregas un nuevo campo a un modelo o modificas la estructura de la base de datos, debes usar este comando para generar las migraciones correspondientes.

13)python manage.py migrate  
Este comando aplica las migraciones generadas previamente a la base de datos. Después de ejecutar makemigrations, es necesario usar migrate para asegurarte de que los cambios en el código se reflejen en la base de datos.

# Diagrama MVT  
1-Cliente envía Request: El cliente o usuario envía una Solicitud (Request) al servidor.  
2-Django: La solicitud llega al servidor donde se está ejecutando Django.  
3-Router Url (Enrutador de URL): Django primero pasa la solicitud a su sistema de enrutamiento de URL (urls.py) y este enrutador se encarga de mapear la URL solicitada a una función específica dentro del View (Vista). 
4-View (Vista): Función o clase de Python que recibe la solicitud y decide qué datos necesita para satisfacer la solicitud y qué Template debe usar para presentarlos. Dos caminos posibles desde aquí:  
   Opcion 1: Si necesita datos: La View interactúa con el Model.  
   Opcion 2: Si ya tiene todos los datos: Pasa directamente al Template.  
5-Model: El Model es la capa que define la estructura de los datos y la lógica para interactuar con la Base de Datos donde la función de View le pide al Model que obtenga, guarde o actualice datos.  
6-Base de Datos: La Model se comunica con la Base de Datos para interactuar con la base de datos, al completar la operación la función de Model devuelve los datos a la función View.  
7-Template: El Template es un archivo HTML (con código especial de Django) que define cómo se verá la página web.  
8-Respuesta al Cliente: Convierte o combina los datos con su estructura HTML para crear la Respuesta final, es decir, una página web completa y se envía al cliente.  

# Explicación de archivos y comandos 
# settigs.py
La función “settings.py” en un proyecto del framework Django, centraliza toda la configuración del proyecto que estemos realizando. Dentro de sus funcionalidades está  la conexión a la base de datos, la configuración de seguridad lo que quiere decir que las configuraciones críticas para la seguridad, como la clave secreta, protección CSRF y la configuración de cookies es gestionada por esta función.  Define aspectos del flujo de trabajo de la aplicación, como los middleware (solicitud y respuesta), la autenticación de usuarios, la gestión de sesiones, entre otras, al igual que la función se encarga de la personalización y la escalabilidad, esto permite ajustarse a nuevos entornos, como el desarrollo y producción.

"""
Django settings for marketplace_main project.

Generated by 'django-admin startproject' using Django 5.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7__w^=9l$(&lv=t4lse(s64__!fe0+gxyi&23^$w2ido6-%no2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
LOGIN_URL = '/store/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Application definition

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


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
 
# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# urls.py
Cuando un usuario accede a una URL de tu sitio, el sistema necesita saber qué código ejecutar para responder a esa solicitud. Esto es exactamente lo que hace el archivo urls.py: mapea las URLs que llegan al servidor con las vistas (o funciones) que deberían ser ejecutadas. De esta forma, cuando un usuario visita una página específica, Django puede dirigir esa solicitud a la vista correspondiente. Cada ruta definida en urls.py asocia una URL con una vista específica de tu aplicación. 
Las vistas son funciones que procesan las solicitudes, interactúan con la base de datos si es necesario, y devuelven una respuesta (generalmente una página web). Así, cuando escribes una URL en tu navegador, Django busca en este archivo para encontrar la vista que debe ejecutar, lo que hace que la navegación de tu sitio sea estructurada y organizada.

En proyectos grandes de Django, no se usa un solo archivo urls.py, sino varios. Cada aplicación dentro del proyecto puede tener su propio archivo urls.py con sus rutas. Luego, existe un archivo principal urls.py que une todas esas rutas usando la función include(). Esto hace que el proyecto sea más ordenado, fácil de entender y mantener, ya que cada parte del sistema gestiona sus propias direcciones sin mezclarse con las demás.

Sin este archivo, el sistema no sabría cómo responder a las diferentes URLs que los usuarios intentan visitar y no podríamos garantizar que la aplicación sea fácil de entender, mantener y expandir, especialmente cuando el proyecto crece en tamaño o complejidad.
"""
URL configuration for marketplace_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# agregar configuraciones para media
from django.conf import settings
from django.conf.urls.static import static
from store.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# models.py
El archivo models.py es esencial para cualquier aplicación en Django, ya que este archivo se crean los modelos, que son clases de Python encargadas de representar las tablas de la base de datos. Cada clase que se define en models.py corresponde a una tabla, y cada uno de sus atributos equivale a una columna dentro de esa tabla. En otras palabras, actúa como el puente entre el código y la base de datos. 
El archivo permite establecer de manera clara y organizada cómo se almacena y se relaciona la información en la base de datos. Django utiliza un sistema llamado ORM (Object-Relational Mapper), que permite al desarrollador interactuar con la base de datos utilizando código Python en lugar de escribir consultas SQL directamente, lo que permite tener un código más ordenado y limpio para que al momento de leerlo o modificarlo. Entre sus otras funciones también, incluir métodos dentro de las clases, los cuales permiten añadir lógica específica relacionada con cada modelo y que las definiciones presentes en models.py para crear y actualizar la base de datos de manera automática, a través de los comandos makemigrations y migrate. 
from django.contrib.auth.models import User
from django.db import models

class Category (models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
class Item (models.Model):
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

# views.py
En un proyecto de Django, cuando el usuario accede a la página y quiere enviar una solicitud, enviar un formulario o realizar alguna acción en el sitio web, Django necesita saber qué acción o que respuesta le dará ante la solicitud enviada por el usuario. Esta tarea o función que se realiza es llamada vistas  (view)

Las vistas son el puente entre los modelos, las plantillas y el usuario. Cuando llega una solicitud HTTP, la vista la recibe, realiza las operaciones necesarias y luego devuelve una respuesta, que puede ser una página HTML, un mensaje JSON o una redirección, según lo que necesite la aplicación. De manera mas sencilla de explicar, como si estuvieras pidiendo un paquete por una pagina web, necesitas que te den respuesta del seguimiento y envias mensaje a las contestadoras automáticas, dependiendo tu problema o solicitud, deben tener una respuesta para tu solicitud. 
 Existen 2 tipos de vistas:
 
Basadas en funciones: Ofrecen estructuras que son directas y sencillas. 
Basada en clases: Que ofrecen una estructura más organizada y facilitan la reutilización de código.

Las vistas son el componente que da vida al sitio web, debido a que permiten que cada acción del usuario que esté en la página,  tenga una respuesta coherente y personalizada según la lógica definida por el desarrollador.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Item, Category
from .forms import SignupForm, NewItemForm

# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories' : categories
    }

    return render(request, 'store/home.html', context)

def contact(request):
    context = {
        'msg': 'Quieres otros productos?'
    }
    return render (request, 'store/contact.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {
        'item' : item,
        'related_item' : related_items
    }
    return render (request, 'store/item.html', context)

def register (request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = SignupForm()

    context = {
        'form' : form
    }
    return render(request, 'store/singup.html', context)

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
        context = {
            'form': form,
            'title': 'New Item'
        }

    return render(request, 'store/form.html', context)

# foder templates/store.
Es la carpeta que almacena todas las páginas html
 templaes\store
  <>base.html
  <>contact.html
  <>home.html
  <>item.html
  <>navegation.html

# Ejecucion del proyecto
Se muestran los items de la pagina web
Tambien se muestra la parte del "Contactanos"
Capturas del "Django administraction para crear las tablas/apartados

# Actualizaciones Del Tercera Parcial 
Forms.py (LoginForm, SignupForm, NewItemForm)
# SignUp y Login en Forms.py
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


from .models import Item


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu usuario',
            'class': 'form-control'
        }
    ))


    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'password',
            'class': 'form-control'
        }
    ))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu Usuario',
            'class': 'form-control'
        }
    ))


    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Tu Email',
            'class': 'form-control'
        }
    ))


    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }
    ))


    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Repite Password',
            'class': 'form-control'
        }
    ))
```

Views.py (login(), logout_user(), detail(), add_item())
# Funciones en views.py
```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout


from .models import Item, Category


from .forms import SignupForm


# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()


    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'store/home.html', context)


def contact(request):
    context = {
        'msg': 'Quieres otros productos contactame!'
    }


    return render(request, 'store/contact.html', context)


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context={
        'item': item,
        'related_items': related_items
    }


    return render(request, 'store/item.html', context)


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)


        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()


    context = {
        'form': form
    }


    return render(request, 'store/signup.html', context)
```



Explicar decorador @login_required
# Login, Register urls.py
```python
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import contact, detail, register


from .forms import LoginForm


urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm)),
    path('detail/<int:pk>/', detail, name='detail'),
]
```

Urls.py (Las rutas a cada acción nueva en views)
# Login, Register urls.py
```python
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import contact, detail, register


from .forms import LoginForm


urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm)),
    path('detail/<int:pk>/', detail, name='detail'),
]
```



store/templates (item.html, login.html, signup.html, navigation.html, form.html)
# Templates templates/store login, signup
```html
{% extends 'store/base.html' %}


{%block title%} {{item.name}}Registro | {%endblock%}


{%block content%}
    <div class="row p-4 d-flex justify-content-center aling-items-center">
        <div class="shadow col-6 bg-#fff p-4 rounded-3">


            <h4 class="mb-6 text-center">Login</h4>
            <hr>
            <!--Formulario de inicio de sesion-->
            <form action="." method="POST">
                {% csrf_token %}
                <div class="mb-3">
                    <label class="form-label">Username:</label>
                    {{form.username}}
                </div>
                <div class="mb-3">
                    <label class="form-label">Username:</label>
                    {{form.password}}
                </div>
                <!-- Captura de errores -->
                {% if form.errors or forms.non_field_errors %}
                    <div class="mb-4 p-6 bg-danger rounded">
                        {% for fields in form%}
                            <h5 class="text-white">
                                {{fields.errors}}
                            </h5>
                        {% endfor %}
                        {{ form.non_field_errors }}
                    </div>
                {% endif %}
                <!--Boton login y registro-->
                <div class="d-flex justify-content-center aling-items-center">
                    <button class="btn btn-primary mb-6">Login</button>
                    </div>
                <div class="d-flex justify-content-center aling-items-center">
                    <a href="{% url 'register' %}">¿No tienes una cuenta? Creala aqui</a>
                </div>
               
            </form>
           
        </div>
    </div>
{%endblock%}
```
```html
{% extends 'store/base.html' %}


{%block title%} {{item.name}}Registro | {%endblock%}


{%block content%}
<div class="row p-4 d-flex justify-content-center aling-items-center ">
    <div class="shadow col-6 bg-#fff p-4 rounded-3">
        <h4 class="mb-6 text-center">Registro</h4>
        <hr>
        <form action="." method="POST">
            {% csrf_token %}
            <div class=" mb-3">
                <label class="form-label">Username:</label>
                {{form.username}}
            </div>
            <div class=" mb-3">
                <label class="form-label">Email:</label>
                {{form.email}}
            </div>
            <div class=" mb-3">
                <label class="form-label">Password:</label>
                {{form.password1}}
            </div>
            <div class=" mb-3">
                <label class="form-label">Repite Password:</label>
                {{form.password2}}
            </div>


            {% if form.errors or forms.non_field_errors %}
                <div class="mb-4 p-6 bg-danger rounded">
                    {% for field in form%}
                        <h5 class="text-white">
                            fields.errors
                        </h5>
                    {% endfor %}
                    {{ form.non_field_errors }}
                </div>
               
            {% endif %}


            <div class="d-flex justify-content-center aling-items-center">
                <button class="btn btn-primary mb-6">Registro</button>
            </div>
            <div class="d-flex justify-content-center aling-items-center">
                <a href="{% url 'login' %}">¿Ya tienes una cuenta? Accesa aqui</a>
            </div>


        </form>
    </div>
</div>
{% endblock %}
```

# Conclusión
El código proporcionado implementa un sistema básico de autenticación y gestión de productos en Django, aprovechando su estructura basada en el patrón MVT (Modelo-Vista-Plantilla).
Formularios (forms.py): El uso de formularios personalizados como LoginForm y SignupForm facilita la recolección de datos del usuario y su validación. Al usar widgets con atributos como class="form-control" y placeholder, el diseño se mantiene consistente y accesible.

Vistas (views.py): La vista register() permite registrar nuevos usuarios, validando los datos del formulario y redirigiendo a la página de login si el registro es exitoso. Por otro lado, la vista detail() gestiona la visualización de detalles de un producto y sugiere productos relacionados. Sin embargo, sería conveniente agregar un decorador @login_required en vistas que deben estar restringidas a usuarios autenticados.

Rutas (urls.py): Las rutas están bien definidas para las páginas de login, registro y detalles de productos. El uso de auth_views.LoginView permite gestionar el login de manera eficiente, pero sería ideal agregar más rutas si se implementan más vistas, como la de agregar productos.

Plantillas (login.html, signup.html, etc.): Las plantillas extendiendo de base.html aseguran que el diseño sea coherente a través de las páginas. Aunque el código es sólido, se debe corregir la forma en que se muestran los errores en los formularios para una experiencia de usuario más clara.

