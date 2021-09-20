import os

from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .models import Symbol


class SymbolIndexView(View):
    def get(self, request):
        context = dict()
        # you can use these variables in index.js
        context["context_for_js"] = {
            'article_base_uri': reverse('article:index'),
            'symbol_base_uri': reverse('symbol:index')
        }
        return render(request, 'symbol/index.html', context)


class SymbolView(View):
    def get(self, request, filename):
        path = os.path.join(Symbol.get_htmlfile_dir(), filename)
        return render(request, path)
