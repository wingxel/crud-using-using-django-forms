from django.urls import path
from . import views

urlpatterns = [
    path("", views.UsersList.as_view(), name="index-page"),
    path("details/<pk>/", views.UserDetails.as_view(), name="details-page")
]
