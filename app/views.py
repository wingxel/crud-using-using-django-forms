from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.handlers.wsgi import WSGIRequest


class IndexView(View):
    def get(self, request: WSGIRequest) -> HttpResponse:
        return render(request, "app/index.html")
