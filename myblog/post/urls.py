from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



# view.py функции
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>/', get_post, name='post_id'),
    path('add_post/', add_post, name='add_post'),
    path('edit_post/<int:id>/', edit_post, name='edit_post'),
    path('delete/<int:id>/', delete_post, name='delete_post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)