from django import urls
from django.urls import include,path
from frontend import views

urlpatterns = [
    path('', views.list, name='list'),
]
