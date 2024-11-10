from django.urls import path
from .views import laboratorio_list, laboratorio_create, laboratorio_edit, laboratorio_delete

urlpatterns = [
    path('', laboratorio_list, name='laboratorio_list'),
    path('create/', laboratorio_create, name='laboratorio_create'),
    path('edit/<int:pk>/', laboratorio_edit, name='laboratorio_edit'),
    path('delete/<int:pk>/', laboratorio_delete, name='laboratorio_delete'),
]