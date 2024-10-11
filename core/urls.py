from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('<int:pk>/', views.details, name='details'),
    path('category/<int:pk>/', views.category, name='category'),
    path('author/<int:pk>/', views.author, name='author'),
] 