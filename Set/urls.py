from django.urls import path
from . import views

urlpatterns = {
        path('set_task/',views.set_task, name='set_task'),
        path('set_user/',views.set_user, name='set_user'), 
        }
