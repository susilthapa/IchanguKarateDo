from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.conf import settings

from django.core.mail import send_mail

from django.views.generic import (
	View,
	TemplateView, 
	ListView,
	DetailView
	)

from .models import(
		Home,
		Contact,
		Events,
		Players,
		ImageSlider,
		Videos,
		Committee,
		Events,

	)


class HomePageView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomePageView, self).get_context_data(*args, *kwargs)
		context['home'] = Home.objects.first()
		return context


class CommitteePageView(TemplateView):
	template_name = 'committee.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CommitteePageView, self).get_context_data(*args, **kwargs)
		context['president'] = Committee.objects.filter(
								Q(position__icontains= 'president') &
								~Q(position__icontains= 'vice')
							).first()

		context['members'] = Committee.objects.exclude(
								Q(position__icontains= 'president') &
								~Q(position__icontains= 'vice')
							)
		return context 


class EventsPageView(ListView):
	model = Events
	template_name = 'events.html'
	context_object_name = 'events'


class EventsDetailPageView(DetailView):
	model = Events
	template_name = 'events_detail.html'
	slug_field = 'slug'
	context_object_name = 'event'

	def get_context_data(self, *args, **kwargs):
		context = super(EventsDetailPageView, self).get_context_data(*args, **kwargs)
		context['details'] = self.object.event_details.all()
		return context


class PlayersPageView(TemplateView):
	template_name = 'players.html'

	def get_context_data(self, *args, **kwargs):
		context = super(PlayersPageView, self).get_context_data(*args, **kwargs)
		context['images'] = ImageSlider.objects.all()
		context['medalists'] = Players.objects.filter(player_type='medalist')
		context['black_belts'] = Players.objects.filter(player_type='black_belt')
		context['players'] = Players.objects.filter(player_type='player')
		return context


class VideosPageView(ListView):
	model = Videos
	template_name = 'videos.html'
	context_object_name = 'videos'


class ContactPagView(TemplateView):
	template_name = 'contact.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ContactPagView, self).get_context_data(*args, *kwargs)
		context['contact'] = Contact.objects.first()
		return context

	def post(self, *args, **kwargs):
		name = self.request.POST.get('name')
		email = self.request.POST.get('email')	
		message = self.request.POST.get('message')			
		
		send_mail(subject='From Ichangu Karate-Do',
					message = f"{name}: {message} via {email}",
					from_email = email,
					recipient_list=['srjthapa53@gmail.com'],
					fail_silently=False
					)

		messages.success(self.request, 'Email has been sent , thank you.')
		return redirect('contact')	



def error_404_view(request, exception):
	return render(request, '404.html', status=404)

def error_500_view(request):
	return render(request, '500.html', status=500)