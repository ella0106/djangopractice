from django.contrib import admin
from django.urls import path
from . import views
from .views import upload_video

urlpatterns = [
    path('post/', views.todo_post, name='todo_post'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    path('done/', views.done_list, name='done_list'),
    path('done/<int:pk>/', views.todo_done, name='todo_done'),
    path('', upload_video, name='upload'),
    path('upload_success/', views.upload_success, name='upload_success'),
]