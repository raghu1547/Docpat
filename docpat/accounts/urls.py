from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [

    path('', views.user_login, name='login'),
    
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    
]
