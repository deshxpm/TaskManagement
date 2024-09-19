from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('tasks/', views.task_list, name='task_list'),
    path('create-task/', views.create_task, name='create_task'),
    path('create-expert/', views.create_expert, name='create_expert'),
    path('bulk-allocation/', views.bulk_allocation, name='bulk_allocation'),
]
