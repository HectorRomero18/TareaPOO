from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='forms'),
    path('tasks/', views.tasks, name='tasks'),
    path('project_tasks/<str:project_id>', views.project_task, name='project_tasks')
]