from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Facility(models.Model):
    # each user has one facility
    user = models.OneToOneField(User)

    # contact information
    name = models.TextField(null=False, blank=False)
    website = models.TextField(null=True, blank=True)  # optional
    phone_number = models.TextField(null=True, blank=True)  # optional
    phone_open_time = models.TimeField(null=True, blank=True)  # optional
    phone_close_time = models.TimeField(null=True, blank=True)  # optional

    # address
    address_line_1 = models.TextField(null=False, blank=False)
    address_line_2 = models.TextField(null=True, blank=True)  # optional
    city = models.TextField(null=False, blank=False)
    state = models.TextField(max_length=2, null=False, blank=False)
    zip_code = models.IntegerField(null=False, blank=False)

    # description
    description = models.TextField(null=False, blank=False)

    # populations to which the facility is restricted

    # familial status (feature)
    children_allowed = models.BooleanField(null=False, blank=False)

    # gender restrictions (features)
    male_only = models.BooleanField(null=False, blank=False)
    female_only = models.BooleanField(null=False, blank=False)

    # focuses (features)
    lgbt_focus = models.BooleanField(null=False, blank=False)
    mental_disability_focus = models.BooleanField(null=False, blank=False)
    physical_disability_focus = models.BooleanField(null=False, blank=False)
    veteran_focus = models.BooleanField(null=False, blank=False)
    pets_allowed = models.BooleanField(null=False, blank=False)

    # other restrictions (features)
    drug_free = models.BooleanField(null=False, blank=False)


# # each Facility can have multiple Human Resources
# class HumanResource(models.Model):
#     facility = models.ForeignKey(Facility)
#
#     name = models.TextField(blank=False, null=False)
#     description = models.TextField(blank=False, null=False)
#
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)
#
#
# # each Human Resource can be offered on multiple days of the week
# class HumanResourceTime(models.Model):
#     human_resource = models.ForeignKey(HumanResource)
#
#     # day of the week is a 0-indexed day starting with Sunday = 0
#     day_of_week = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(0)],
#                                       null=False, blank=False)
#     start_time = models.TimeField(null=False, blank=False)
#     end_time = models.TimeField(null=False, blank=False)
#
#     # silly rabbit, trix are for kids
#     class Meta:
#         unique_together = ('human_resource', 'day_of_week', 'start_time', 'end_time')


# features are universal, and are only changed by site admins
class PrimarySecondaryNeed(models.Model):
    # each facility can meet multiple needs, each need can be applicable to multiple facilities
    facilities = models.ManyToManyField(Facility)

    name = models.TextField(blank=False, null=False)
    big_image = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)


class Commodity(models.Model):
    facility = models.ForeignKey(Facility)

    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    # 2 = in stock, 1 = low stock, 0 = out of stock
    stock_level = models.IntegerField(null=False, blank=False,
                                      validators=[MinValueValidator(0), MaxValueValidator(2)])

