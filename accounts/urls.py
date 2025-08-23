from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, UserDeleteView
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/account_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='registration/account_register.html'), name='register'),
    path('konto/usun/', UserDeleteView.as_view(), name='delete-account'),
    path('konto/usuniete/', TemplateView.as_view(template_name='registration/user_deleted.html'), name='user-deleted'),
]
