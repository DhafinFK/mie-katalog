from django.urls import path
from . import views

app_name = "mie"
urlpatterns = [
  path('', views.show_katalog, name="katalog",)
]