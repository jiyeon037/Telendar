from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='data_home'),
    path('kategorie/', views.kategorie, name='data_kategorie'),
    path('theme/<str:theme_title>/', views.theme_detail, name="data_theme_detail"),
    path('theme_add/<str:theme_title>/', views.theme_add, name ="data_theme_add"),
]