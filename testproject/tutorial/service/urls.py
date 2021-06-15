from django.urls import path
from .views import home, add_service, view_service, edit_service, delete_service

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_service, name='add_post'),
    path('service/<int:pk>', view_service, name='view_service'),
    path('edit/<int:pk>', edit_service, name='edit'),
    path('delete/<int:pk>', delete_service, name='delete'),
]