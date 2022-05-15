from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('owner/<int:owner_id>/', views.owner, name="owner"),
    path('dog/<int:dog_id>/', views.dog, name="dog"),
]
