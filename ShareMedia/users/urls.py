from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.user_reg, name='regd'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
