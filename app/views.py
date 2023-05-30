from django.views.generic import ListView, DetailView

from app.models import User


class UsersList(ListView):
    template_name = "app/index.html"
    context_object_name = "users_list"
    
    def get_queryset(self):
        return User.objects.values("username", "id")


class UserDetails(DetailView):
    model = User
    template_name = "app/details.html"
    context_object_name = "user"
