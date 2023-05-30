from django.urls import path
from . import views

urlpatterns = [
    path("", views.UsersList.as_view(), name="index-page"),
    path("details/<int:pk>/", views.UserDetails.as_view(), name="details-page"),
    path("add-user/", views.CreateUser.as_view(), name="add-user"),
    path("update-user/<int:pk>/", views.UpdateUser.as_view(), name="update-user"),
    path("delete/<int:pk>/", views.DeleteUser.as_view(), name="delete-user")
]
