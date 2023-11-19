from django.urls import path
from . import views

app_name = 'log'

urlpatterns = [
    path('index', views.func, name = 'index'),
    path('<str:book>', views.func2, name = 'book-details')
]