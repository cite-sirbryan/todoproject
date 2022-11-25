from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('chart/', views.chartTask, name="chart"),
    path('search/', views.searchTask, name="search"),
]