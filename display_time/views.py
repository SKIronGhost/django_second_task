from django.shortcuts import HttpResponse, render
from time import gmtime, strftime


def display_time(request):

    context = {
        "time": strftime("%H:%M %p", gmtime(-4)),
        "date": strftime("%B %d, %Y", gmtime())
    }
    return render(request, 'index.html', context)
