from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('guitars/', views.index, name="index"),
    path('guitars/create/', views.CreateGuitar.as_view(), name="create"),
    path('guitars/<int:guitar_id>/', views.detail, name="detail"),
    path('guitars/<int:pk>/edit/', views.UpdateGuitar.as_view(), name="update"),
    path('guitars/<int:pk>/delete/', views.DeleteGuitar.as_view(), name="delete"),
]
