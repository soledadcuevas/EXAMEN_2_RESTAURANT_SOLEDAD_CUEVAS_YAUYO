from django.urls import path
from . import views

urlpatterns = [
    path('clientes_list/', views.clientes_list, name='clientes_list'),
]