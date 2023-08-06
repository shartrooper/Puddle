from django.urls import path

from . import views

#namespace
app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]
