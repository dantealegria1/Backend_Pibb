from django.urls import path
from . import views

urlpatterns = {
        path('delete_task/',views.delete_task, name='delete_task'),
        path('delete_user/',views.delete_user, name='delete_user'),
        
        }
