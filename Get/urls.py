from django.urls import path
from . import views

urlpatterns = {
        path('get_task/',views.get_task, name='get_task'),

        path('get_user/',views.get_user, name='get_user'),

        
        }
