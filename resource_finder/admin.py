from django.contrib import admin

# Register your models here.
from resource_finder.models import Facility, PrimarySecondaryNeed, Commodity

admin.site.register(Facility)
admin.site.register(PrimarySecondaryNeed)
admin.site.register(Commodity)