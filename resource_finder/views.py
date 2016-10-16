from django.http.response import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from resource_finder.models import PrimarySecondaryNeed, Facility


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


def create_account(request):
    if request.method == "GET":
        return render(request, 'resource_finder/facility/create_account.html')
    else:
        return HttpResponse("No soup for you!")


def view_facility(request, facility_id):
    try:
        facility = Facility.objects.get(id=facility_id)
    except Facility.DoesNotExist:
        raise Http404

    context = {
        'facility': facility,
        'features': facility.primarysecondaryneed_set.all().order_by('name'),
        'commodities': facility.commodity_set.all().order_by('name')
    }

    if facility.website:
        if facility.website.startswith("http://") or facility.website.startswith("https://"):
            website = facility.website
        else:
            website = "http://" + facility.website

        context['website'] = website

    return render(request, 'resource_finder/facility/view_facility.html', context)


def give_to_facility(request):

    possible_donations = ""

    facilities = Facility.objects.all()

    fac_for_template = []

    for facility in facilities:
        if request.GET.get('donate'):
            possible_donations = request.GET.get('donate')

            commodities_out = facility.commodity_set.filter(stock_level=0, name__contains=possible_donations)
            commodities_low = facility.commodity_set.filter(stock_level=1, name__contains=possible_donations)

        else:
            commodities_out = facility.commodity_set.filter(stock_level=0)
            commodities_low = facility.commodity_set.filter(stock_level=1)

        fac_for_template.append({
            'name': facility.name,
            'id': facility.id,
            'commodities_out': commodities_out,
            'commodities_low': commodities_low
        })

    context = {
        'facilities': fac_for_template,
        'old_query': possible_donations
    }

    return render(request, 'resource_finder/give_resources/facility_list.html', context)


def list_relevant_facilities(request):
    switches = []
    for a in request.GET:
        switches += a

    facilities = Facility.objects.all()

    fac_for_template = []

    for f in facilities:
        yes = f.primarysecondaryneed_set.filter(id__in=switches)
        if len(yes) != 0:
            fac_for_template.append({
                'name': f.name,
                'id': f.id,
                'description': f.description,
                'resources': f.primarysecondaryneed_set
            })

    context = {
        'facilities': facilities
    }

    return render(request, 'resource_finder/get_resources/facility_list.html', context)