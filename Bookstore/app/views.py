from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls  import reverse

# Create your views here.

# def func(request):
#     return HttpResponse('Welcome to Django')

d = {'HP':{'cat' : 'adv'},
     'FS':{'cat' : 'sex'},
     'WOF':{'cat' : 'moti'},
}



def func(request):
    return render(request, "htmls\home.html", {'data':d})

def func2(request, day):
    day = day
    c = list(d)
    print(d)
    return render(request, "htmls\details.html", {'data':d, 'c':c, 'day':day})