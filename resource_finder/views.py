from django.shortcuts import render

# Create your views here.
from resource_finder.models import PrimarySecondaryNeed


def index(request):
    context = {
        'name': 'Sam'
    }
    return render(request, 'resource_finder/index.html', context)


def primary_needs(request):
    context = {
        'primary_needs': PrimarySecondaryNeed.objects.all().order_by('name')
    }

    return render(request, 'resource_finder/get_resources/primary_needs.html', context)
