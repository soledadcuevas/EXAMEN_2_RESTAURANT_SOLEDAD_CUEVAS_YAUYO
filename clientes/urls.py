from django.urls import path
from . import views

urlpatterns = [
    path('clientes_list/', views.clientes_list, name='clientes_list'),
    path('clientes_orm/', views.clientes_orm, name='clientes_orm'),
    path('clientes_search/', views.clientes_search, name='clientes_search'),
    path('clientes_details/', views.clientes_details, name='clientes_details'),
    path('clientes_delete/<int:id_clientes>', views.clientes_delete, name='clientes_delete'),
    path('clientes_edit/<int:id_clientes>', views.clientes_edit, name='clientes_edit'),
    path('clientes_create/', views.clientes_create, name='clientes_create'),
    #path('clientes_list_vc/', views.ClientesList.as_views(), name="clientes_list_vc"),
    #path('clientes_create_vc/', views.ClientesCreate.as_views(), name="clientes_create_vc"),
    #path('clientes_detail/<int:id_clientes>', views.clientes_detail, name="clientes_edit"),
    path('clientes_list_drf_def/', views.clientes_api_view, name="clientes_list_drf_def"),
    path('clientes_detail_drf_def/<int_pk>', views.clientes_details_view, name="clientes_detail_drf_def"),
]