from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name': 'Sam'
    }
    return render(request, 'resource_finder/index.html', context)

