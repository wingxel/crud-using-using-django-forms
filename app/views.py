from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.libs.custom_forms import AddUserForm, UpdateUserForm
from django.urls import reverse_lazy
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseBadRequest
from django.db.models import Q
from django.shortcuts import render

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


class Search(View):
    def get(self, request: WSGIRequest) -> HttpResponse:
        query_term = request.GET["s"]
        if len(query_term) > 0:
            query_list = Q(username__icontains=query_term) | Q(email__icontains=query_term) | Q(location__icontains=query_term)
            if query_term.isdigit():
                query_list |= Q(id=query_term)
            results = User.objects.filter(query_list)
            return render(request, "app/search_results.html", {
                "results": results,
                "s": query_term
            })
        return HttpResponseBadRequest("Bad Request")
