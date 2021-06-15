from django.urls import path
from .views import ServiceListView, AboutTemplateView, ServiceDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ServiceListView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('post/<int:pk>/', ServiceDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

