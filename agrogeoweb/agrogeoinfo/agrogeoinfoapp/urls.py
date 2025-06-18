from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('staticmap/', views.map_view, name='map_view'),
    path('fermes/', views.MainView.as_view(), name='fermes'),
    path('fermes/sensors/sensor', views.map_view, name='sensor'),
]