from django.urls import path

from . import views

urlpatterns = [
    path('getData', views.GetData.as_view(), name='getData'),
]
