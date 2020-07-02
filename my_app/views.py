from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
	template_name = 'index.html'

class ContactPagView(TemplateView):
	template_name = 'contact.html'

class GalleryPageView(TemplateView):
	template_name = 'gallery.html'

class CommitteePageView(TemplateView):
	template_name = 'committee.html'

class EventsPageView(TemplateView):
	template_name = 'events.html'
