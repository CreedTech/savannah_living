from app.models import LivingOptions,House,Career
from django.shortcuts import render,redirect

def options_renderer(request):
    living_options = LivingOptions.objects.all().order_by('-date_posted') if LivingOptions.objects.all().count() > 0 else None
    houses = House.objects.all().order_by('-date_posted') if House.objects.all().count() > 0 else None
    careers = Career.objects.all().order_by('-date_posted') if Career.objects.all().count() > 0 else None

    return {
      'living_options': living_options,
      'houses': houses,
      'careers': careers,
    }