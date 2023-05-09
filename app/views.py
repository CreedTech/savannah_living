from django.shortcuts import render,redirect

from app.models import House, LivingOptions,Career
from django.views import View

# Create your views here.


def index(request):
    template_name = 'pages/index.html'
    return render(request, template_name)


def about(request):
    template_name = 'pages/about.html'
    return render(request, template_name)


def contact(request):
    template_name = 'pages/contact.html'
    return render(request, template_name)


# def faqs(request):
#     template_name = 'pages/faqs.html'
#     return render(request, template_name)

def services(request):
    template_name = 'pages/services.html'
    return render(request, template_name)

def careers(request):
    template_name = 'pages/careers.html'
    try:
      careers = Career.objects.all().order_by('-date_posted')

    except Career.DoesNotExist:
      return redirect('handler404')   
    context = {
      'careers': careers,
    }
    return render(request,template_name,context)

def career_detail_view(request,slug):
    template_name = 'pages/career_details.html'
    try:
        career = Career.objects.get(slug=slug)
    except Career.DoesNotExist:
        return redirect('handler404')
    context = {
        'career': career
    }
    return render(request,template_name,context)

def living_options(request):
    template_name = 'pages/living_options.html'
    try:
      living_options = LivingOptions.objects.all().order_by('-date_posted')

    except LivingOptions.DoesNotExist:
      return redirect('handler404')   
    context = {
      'living_options': living_options,
    }
    return render(request,template_name,context)

# class LivingOptionDetailView(View):
#     model = LivingOptions
#     template_name = 'pages/single_living_options.html'
#     context_object_name = 'living_option'
#     slug_field = 'slug'

#     def post(self, slug):
#         living_option = LivingOptions.objects.get(slug=slug)
#         return redirect('living_option', slug=living_option.slug)

def single_living_option(request,slug):
    template_name = 'pages/single_living_options.html'
    try:
        living_option = LivingOptions.objects.get(slug=slug)
    except LivingOptions.DoesNotExist:
        return redirect('handler404')
    context = {
        'living_option': living_option
    }
    return render(request,template_name,context)

def communities(request):
    template_name = 'pages/communities.html'
    try:
      houses = House.objects.all().order_by('-date_posted')

    except House.DoesNotExist:
      return redirect('handler404')
    context = {
      'houses': houses,
    }
    return render(request,template_name,context)
def single_community(request,slug):
    template_name = 'pages/single_community.html'
    try:
        house = House.objects.get(slug=slug)
    except House.DoesNotExist:
        return redirect('handler404')
    context = {
        'house': house
    }
    return render(request,template_name,context)

def schedule_visit(request):
    template_name = 'pages/schedule_visit.html'
    return render(request,template_name)

def handler404(request,exception):
    template_name = '404.html'
    return render(request,template_name,status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)