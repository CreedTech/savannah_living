from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('faqs/', views.faqs, name="faqs"),
    path('services/', views.services, name="services"),
    path('careers/', views.careers, name="careers"),
    path('career/<slug:slug>/', views.career_detail_view, name="career"),
    path('about/', views.about, name="about"),
    path('livings/', views.living_options, name="livings"),
    path('living/<slug:slug>/', views.single_living_option, name='living'),
    path('admissions/', views.communities, name="admissions"),
    path('admission/<slug:slug>/', views.single_community, name='admission'),
    path('schedule_visit/', views.schedule_visit, name="schedule_visit"),
    path('contact/', views.contact, name="contact"),
    path('404/', views.handler404, name='handler404')
]