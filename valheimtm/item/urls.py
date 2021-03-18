from django.urls import path

from . import views

urlpatterns = [
    path('gg/', views.index, name='index'),
]