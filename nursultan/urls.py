from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/<int:test_id>/', views.test, name='pass-test'),
    path('create-test/', views.create_test, name='create-test'),
]