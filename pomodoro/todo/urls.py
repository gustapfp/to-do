from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update-task/<str:pk>/', views.updateTasks, name='update-task'),
    path('delete/<str:pk>/', views.deleteTasks, name='delete')
]