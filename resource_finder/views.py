from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name': 'Sam'
    }
    return render(request, 'resource_finder/index.html', context)


def primary_needs(request):
    context = {

    }

    return render(request, 'resource_finder/get_resources/primary_needs.html', context)
