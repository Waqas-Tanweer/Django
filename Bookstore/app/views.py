from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls  import reverse

# Create your views here.

def func(request):
    return render(request, "htmls\home.html")