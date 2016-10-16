from django.contrib import admin

# Register your models here.
from resource_finder.models import Facility, PrimarySecondaryNeed

admin.site.register(Facility)
admin.site.register(PrimarySecondaryNeed)
