from django.urls import path
from . import views
urlpatterns = [
    path('platos_list/', views.platos_list, name='platos_list')
]