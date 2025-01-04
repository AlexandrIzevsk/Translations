from django.http.response import HttpResponse
# from django.shortcuts import render
from django.utils.translation import gettext as _  # импортируем функцию для перевода
from django.views import View


# Create your views here.

class Index(View):
    def get(self, request):
        string = _('Hello world')

        return HttpResponse(string)


# from django.http import HttpResponse
# from django.utils.translation import gettext as _
#
# def my_view(request):
#     output = _("Welcome to my site.")
#     return HttpResponse(output)