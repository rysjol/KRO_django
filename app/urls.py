from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cat/<int:id>', views.category, name='category'),
    path('cat/', views.categories, name='categories')
]