from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("results", views.display_results, name="display_results"),
    path("", views.home, name="home"),
    url(r"^admin/", admin.site.urls),
    url(
        r"^accounts/login/$",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
]
