from django.urls import path 
from .views import * 
urlpatterns = [
    path('',home),
    path('add',addstaff),
    path('staff/<int:pk>',staff),
    path('remove/<int:pk>',removestaff),
]