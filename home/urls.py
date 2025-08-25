from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.Homepage.as_view(), name='home'),
    path("about", views.AboutPage.as_view(), name='about'),
    path("contact", views.ContactPage.as_view(), name='contact'),
    path("plans", views.PlanPage.as_view(), name='plan'),
]