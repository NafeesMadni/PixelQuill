from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
