from django.urls import path
from . import views
urlpatterns = [
    path('', views.Summary),
    path('about/', views.about, name="about"),
]