from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('guitars', views.index, name="index"),
    path('guitars/create/', views.CreateGuitar.as_view(), name="create"),
]
