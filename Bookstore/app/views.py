from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def func(request):
    return HttpResponse("<h2 style='text-align:center'>Welcome to my Django Project</h2>")