from django.urls import path
from . import views

urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_orm/', views.meseros_orm, name='meseros_orm'),
    path('meseros_search/', views.meseros_search, name='meseros_search'),
    path('meseros_details/', views.meseros_details, name='meseros_details'),
    path('meseros_delete/<int:id_meseros>', views.meseros_delete, name='meseros_delete'),
    path('meseros_edit/<int:id_meseros>', views.meseros_edit, name='meseros_edit'),
    path('meseros_create/', views.meseros_create, name='meseros_create'),
    #path('meseros_list_vc/', views.MeserosList.as_views(), name="meseros_list_vc"),
    path('meseros_list serializer/', views.ListMeserosSerializer, name="meseros_list_ssr"),
    path('meseros_list_drf_def/', views.meseros_api_view, name="meseros_list_drf_def"),
    path('meseros_detail_drf_def/<int:pk>', views.meseros_details_view, name="meseros_detail_drf_def"),
]