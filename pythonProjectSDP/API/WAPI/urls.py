from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='WAPI-home'),
    path('login/', views.login, name='WAPI-login'),
    path('register/', views.register, name='WAPI-register'),
    path('home/', views.home, name='WAPI-home'),
    path('home/forecast/', views.forecast, name='WAPI-forecast'),
    path('mumbai/', views.mumbai, name='WAPI-mumbai'),
    path('delhi/', views.delhi, name='WAPI-delhi'),
    path('bangalore/', views.bangalore, name='WAPI-bangalore'),
    path('kolkata/', views.kolkata, name='WAPI-kolkata'),
]
