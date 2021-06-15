from django.urls import path
from .views import (ServiceListView, ServiceDetailView,
                    ServiceCreateView, ServiceUpdateView,
                    ServiceDeleteView)

urlpatterns = [
    path('', ServiceListView.as_view(), name='home'),
    path('detail/<int:pk>/', ServiceDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/update/', ServiceUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/delete/', ServiceDeleteView.as_view(), name='delete'),
    path('add_service/', ServiceCreateView.as_view(), name='add_service'),
]