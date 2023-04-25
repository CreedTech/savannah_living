from app.models import LivingOptions
from django.shortcuts import render,redirect

def options_renderer(request):
    living_options = LivingOptions.objects.all().order_by('-date_posted') if LivingOptions.objects.all().count() > 0 else None

    return {
      'living_options': living_options,
    }