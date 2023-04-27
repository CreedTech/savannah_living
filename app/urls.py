from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('faqs/', views.faqs, name="faqs"),
    path('services/', views.services, name="services"),
    path('about/', views.about, name="about"),
    path('livings/', views.living_options, name="livings"),
    path('living/<slug:slug>/', views.single_living_option, name='living'),
    path('communities/', views.communities, name="communities"),
    path('community/<slug:slug>/', views.single_community, name='community'),
    path('schedule_visit/', views.schedule_visit, name="schedule_visit"),
    path('contact/', views.contact, name="contact"),
    path('404/', views.error_page, name='error_page')
]