from django.urls import path
from . import views

app_name = 'log'

urlpatterns = [
    path('index', views.func),
    path('<str:day>', views.func2, name = 'book-details')
]