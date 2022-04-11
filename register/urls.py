from django.urls import path, include

from . import views
from register import views as register_v

urlpatterns = [
    path('register/', register_v.register, name="register"),
    path('password_change/', register_v.PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('', include("django.contrib.auth.urls")),
    path('password_reset/', register_v.PasswordsResetView.as_view(template_name='registration/password_reset_form.html')),
]