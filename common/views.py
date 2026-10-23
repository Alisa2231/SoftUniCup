from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'common/home.html'
    extra_context = {
        'page_title': 'SoftUni Cup | Play for Glory'
    }