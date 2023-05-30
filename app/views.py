from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.libs.custom_forms import AddUserForm, UpdateUserForm
from django.urls import reverse_lazy

from app.models import User


class UpdateUser(UpdateView):
    model = User
    template_name = "app/update_user.html"
    form_class = UpdateUserForm


class CreateUser(CreateView):
    template_name = "app/add_user.html"
    form_class = AddUserForm


class DeleteUser(DeleteView):
    model = User
    success_url = reverse_lazy("index-page")


class UsersList(ListView):
    template_name = "app/index.html"
    context_object_name = "users_list"
    
    def get_queryset(self):
        return User.objects.order_by("id").values("id", "username")


class UserDetails(DetailView):
    model = User
    template_name = "app/details.html"
    context_object_name = "user"
