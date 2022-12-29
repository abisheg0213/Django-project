from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.display,name="display"),
    path('view/<str:pk>',views.projectdis,name='view'),
    path('createproj',views.create_project,name="create_project"),
    path('update_project/<str:pk>',views.update_project,name="updateproj"),
    path('delete/<str:pk>',views.delete_project,name="deleteproject")
]
