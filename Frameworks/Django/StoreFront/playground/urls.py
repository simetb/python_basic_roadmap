from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),  # Ejemplo de ruta en playground
    # Otras rutas de playground aquí...
]