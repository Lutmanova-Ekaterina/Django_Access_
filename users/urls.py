
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from users.apps import UsersConfig
from users.views import CustomLoginView, UserEditProfileView, CustomRegisterView, ActivateAccount

app_name = UsersConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html',
             subject_template_name='users/password_reset_subject.txt',
             email_template_name='users/password_reset_email.html',
             success_url='done/'), name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete')
]
