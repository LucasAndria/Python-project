from django.contrib import admin
from django.urls import path
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.listeAll, name="listeEnseignantHome"),
    path('liste/', views.listeAll, name="listeEnseignantHome")
]
