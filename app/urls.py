from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('faqs/', views.faqs, name="faqs"),
    path('about/', views.about, name="about"),
    path('living_options/', views.living_options, name="living_options"),
    path('living_options/<slug:slug>/', views.single_living_option, name='living_option'),
    path('communities/', views.communities, name="communities"),
    path('single_community/<slug:slug>/', views.single_community, name='community'),
    path('schedule_visit/', views.schedule_visit, name="schedule_visit"),
    path('contact/', views.contact, name="contact"),
    path('404/', views.error_page, name='error_page')
]