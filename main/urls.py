from django.urls import path

from . import views

urlpatterns = [

    path('home/', views.home, name="home"),
    path('base/', views.base, name="base"),
]