from django.urls import path
from . import views

urlpatterns = [
    # user

    path('',views.log),
    path('register',views.reg),
    path('home',views.home),
]