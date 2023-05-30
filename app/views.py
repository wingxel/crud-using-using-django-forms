from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from app.libs.custom_forms import AddUserForm, UpdateUserForm

from app.models import User


class UpdateUser(UpdateView):
    model = User
    template_name = "app/update_user.html"
    form_class = UpdateUserForm


class CreateUser(CreateView):
    template_name = "app/add_user.html"
    form_class = AddUserForm


class UsersList(ListView):
    template_name = "app/index.html"
    context_object_name = "users_list"
    
    def get_queryset(self):
        return User.objects.values("username", "id")


class UserDetails(DetailView):
    model = User
    template_name = "app/details.html"
    context_object_name = "user"
