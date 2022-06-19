from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('business/',views.business, name='business'),
    path('emergency/',views.contact, name='emergency'),
    path('register/',views.register, name='register'),
]