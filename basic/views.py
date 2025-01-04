from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _  # импортируем функцию для перевода
from django.views import View
# from django.utils.translation import activate, get_supported_language_variant, LANGUAGE_SESSION_KEY


# Create your views here.

class Index(View):
    def get(self, request):
        string = _('Hello world')
        # string = 'Hello world'

        context = {
            'string': string
        }

        return HttpResponse(render(request, 'index.html', context))
