from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.sign_in, name = 'login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('auth_app/', views.auth_app, name='auth_app'),

]