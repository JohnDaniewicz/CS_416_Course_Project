from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutPage, name='logout'),  # changed to logoutPage so this url connects to my new method
    path('game/', views.gamePage, name='game'),
]