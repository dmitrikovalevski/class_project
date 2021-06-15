from django.urls import path

from .views import UserFormView, UserLogIn, UserLogOut,\
    UserAccountListView, PasswordReset, PasswordResetConfirm,\
    PasswordResetDone, PasswordResetComplete

urlpatterns = [
    path('add/', UserFormView.as_view(), name='add_user'),
    path('login/', UserLogIn.as_view(), name='login'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    path('account/', UserAccountListView.as_view(), name='account'),
    path('forgot/', PasswordReset.as_view(), name='forgot'),
    path('reset_confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset_done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('change_your_password/', PasswordResetComplete.as_view(), name='password_reset_complete')
]