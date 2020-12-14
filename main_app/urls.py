from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('guitars/', views.index, name="index"),
    path('guitars/create/', views.CreateGuitar.as_view(), name="create"),
    path('guitars/<int:guitar_id>/', views.detail, name="detail"),
    path('guitars/<int:pk>/edit/', views.UpdateGuitar.as_view(), name="update"),
    path('guitars/<int:pk>/delete/', views.DeleteGuitar.as_view(), name="delete"),
    path('guitars/<int:guitar_id>/add_maintenance/', views.add_maintenance, name="add_maintenance"),
    path('guitars/<int:guitar_id>/add_accessory/', views.add_accessory, name="add_accessory"),
    path('guitars/<int:guitar_id>/remove_accessory/<int:accessory_id>/', views.remove_accessory, name="remove_accessory"),
    path('accessories/', views.AccessoriesList.as_view(), name="accessory_index"),
    path('accessories/create/', views.AccessoriesCreate.as_view(), name="accessory_create"),
    path('accessories/<int:pk>/', views.AccessoriesDetail.as_view() ,name="accessory_detail"),
    path('accessories/<int:pk>/edit/', views.AccessoriesUpdate.as_view(), name="accessory_update"),
    path('accessories/<int:pk>/delete/', views.AccessoriesDelete.as_view(), name="accessory_delete"),
    
]
