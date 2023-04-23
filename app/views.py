from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = 'pages/index.html'
    return render(request,template_name)

def about(request):
    template_name = 'pages/about.html'
    return render(request,template_name)

def contact(request):
    template_name = 'pages/contact.html'
    return render(request,template_name)

def faqs(request):
    template_name = 'pages/faqs.html'
    return render(request,template_name)

def living_options(request):
    template_name = 'pages/living_options.html'
    return render(request,template_name)

def single_living_option(request,slug):
    template_name = 'pages/single_living_options.html'
    return render(request,template_name)

def communities(request):
    template_name = 'pages/communities.html'
    return render(request,template_name)

def single_community(request,slug):
    template_name = 'pages/single_community.html'
    return render(request,template_name)

def schedule_visit(request):
    template_name = 'pages/schedule_visit.html'
    return render(request,template_name)

def error_page(request):
    template_name = 'pages/404.html'
    return render(request,template_name)