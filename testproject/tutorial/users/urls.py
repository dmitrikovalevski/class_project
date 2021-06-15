from django.urls import path
from .views import user_account, create_user, login_user, logout_user, update_account, ChangePasswordP4
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('account/', user_account, name='account'),
    path('register/', create_user, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('update/', update_account, name='update'),
    path('forgot/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_complete/', ChangePasswordP4.as_view(), name='password_reset_complete'),

]



