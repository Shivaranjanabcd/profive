from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services", views.service, name="services"),
    path("it_infra_service", views.it_infra_service, name="it_infra_service"),
    path("cloud_service", views.cloud_service, name="cloud_service"),
    path("contact", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("project", views.project, name="project"),
    path("about", views.about, name="about"),
    path("manged_it", views.manged_it, name="manged_it"),
]
