from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls  import reverse

# Create your views here.

# def func(request):
#     return HttpResponse('Welcome to Django')

d = {
    'Harry Potter': ['Adventure', '1200'],
    'Fifty Shades': ['Fantasy', '500'],
    'Wings of Fire': ['Motivation', '1800'],
}



def func(request):
    return render(request, "htmls\home.html", {'data':d})