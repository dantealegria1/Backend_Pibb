from django.urls import path
from . import views

urlpatterns = {
        path('get/',views.get_task, name='get_task'),
        path('set/',views.set_task, name='set_task')
        }
