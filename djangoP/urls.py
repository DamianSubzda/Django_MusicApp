"""djangoP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as register_v

from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('base/', views.base, name="home"),
    path('profile/', views.profile, name="profile"),
    path('payU/', views.payU),
    path('register/', register_v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('password/', register_v.PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_reset/', register_v.PasswordsResetView.as_view(template_name='registration/password_reset_form.html')),

]