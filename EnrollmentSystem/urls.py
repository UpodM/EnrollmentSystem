from django.urls import path
from . import views

urlpatterns = [
    path('user', views.index_user),
]
