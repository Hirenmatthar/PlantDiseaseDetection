from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login_view/', views.login_view, name='login_view'),
    path('register_view/', views.register_view, name='register_view'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]