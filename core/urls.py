from django.urls import path
from . import views

urlpatterns = [
    path('results', views.display_results, name='display_results'),
    path('', views.home, name='home'),
]
