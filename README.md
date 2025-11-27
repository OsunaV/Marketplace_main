# Nombre del poryecto: Markeplace

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

# Funcionalidad para que el usuario agregue articulos en la aplicacion siempre y cuando tenga acceso a la aplicacion store, estos son los pasos:
1.actualice el archivo forms.py a el final del archivo
```py
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 100px'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
```
2.Actualice el archivo views.py con la siguiente linea de codigo para el decorador en la linea 2 de su codigo.
```py 

from django.contrib.auth.decorators import login_required
```

3.En el mismo archivo views.py ponga la siguiente funcion a el final del archivo
```py
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
```
4.Cree un archivo en 'templates/store' llamado form.html y agregue el siguiente codigo:
```html

{% extends 'store/base.html' %}

{% block title %} {{ title }} {% endblock %}

{% block content%}
    <h4 class="mb-4 mt-4">{{ title }}</h4>
    <hr>
    <form action="." method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <div>
        
            {{ form.as_p }}
        </div>

        {% if form.errors or form.non_field_errors %}
            <div class="mb-4 p-6 bg-danger">
                {% for field in form %}
                    {{ field.errors }}
                {% endfor %}

                {{ form.non_field_errors }}
            </div>
        {% endif %}

        <button class="btn btn-primary mb-6">Register</button>
    </form>
{% endblock%}
```
5.Actualice el archivo urls.py en la aplicacion store con la siguiente ruta:
```py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import contact, detail, register, logout_user, add_item

from .forms import LoginForm

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_item/', add_item, name='add_item'),
    path('detail/<int:pk>/', detail, name='detail'),
]
```
6.Actualice el archivo navigation.html para que el usuario pueda navegar a la forma de agregar articulo
```html
<nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
    <div class="container-fluid">
        <a href="{% url 'home' %}" class="navbar-brand">Marketplace</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-control="navBarNav" aria-expanded="false" aria-label="Toggle Navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a href="" class="nav-link active">
                        Home
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{% url 'contact' %}" class="nav-link active">
                        Contact
                    </a>
                </li>
               
                {% if request.user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'add_item'%}">Add Item</a>
                    </li>
                    <li class="nav-item">
                        <a href="{% url 'logout' %}" class="nav-link active">
                            Logout
                        </a>
                    </li>
                {% else %}
                    <li class="nav-item">
                        <a href="{% url 'login' %}" class="nav-link active">
                            Login
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="{% url 'register' %}" class="nav-link active">
                            Register
                        </a>
                    </li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
```
Documentacion cumpleta(Desde Primer Parcial al Tercer Parcial)(27/11/25)
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
