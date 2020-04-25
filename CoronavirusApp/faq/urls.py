from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Articles

urlpatterns = [
    path('',
         ListView.as_view(queryset=Articles.objects.all(),
                          template_name="faq/faqPage.html")),
]
