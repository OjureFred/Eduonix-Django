from django.urls import path

from . import views

app_name="profiles"

urlspatterns = [
    path("profile/<str:usernamr>/", views.ProfileDetailView.as_view(), name="detail"),
]