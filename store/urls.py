from django.urls import path
from .views import contact, detail

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('details/<int:pk>/', detail, name='detail')
    ]