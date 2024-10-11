from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'app/homepage.html'

class AboutPageView(TemplateView):
    template_name = 'app/aboutpage.html'

class ItemPageView(TemplateView):
    template_name = 'app/itemspage.html'

class ContactPageView(TemplateView):
        template_name = 'app/contactpage.html'