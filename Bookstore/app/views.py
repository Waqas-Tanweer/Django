from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls  import reverse

# Create your views here.

# def func(request):
#     return HttpResponse('Welcome to Django')

d = {'HP':{'category' : 'adventure', 'price' : 800 , 'ratings' : 8.6},
     'FS':{'category' : 'fantasy', 'price' : 500, 'ratings' : 5.8},
     'WOF':{'category' : 'motivational', 'price' : 1200, 'ratings' : 9.3},
}





def func(request):
    return render(request, "htmls\home.html", {'data':d})

def func2(request, book):
    book = book
    print(d)
    return render(request, "htmls\details.html", {'data':d, 'book':book, 'l': d[book], })