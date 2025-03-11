from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts_home, name='accounts_home'),
    path('add_accounts', views.add_accounts, name='add_accounts'),
    path('get_game/', views.get_game, name = 'get_game'),
    path('get_account/', views.log_to_acc, name = 'accounts_get'),
    path('change_status_false/', views.change_status_false, name='change_status_false'),
    path('change_status_true/', views.change_status_true, name='change_status_true'),

]