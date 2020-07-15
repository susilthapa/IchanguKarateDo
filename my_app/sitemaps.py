from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from my_app.models import *


class HomeSitemap(Sitemap):
	changefreq = "monthly"
	priority = 1.0

	def items(self):
		return Home.objects.all()

	def location(self, item):
		return reverse('home')


class EventsSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.9
	def items(self):
		return Events.objects.all()

class CommitteeSitemap(Sitemap):
	changefreq = "yearly"
	priority = 0.7

	def items(self):
		return Committee.objects.all()

	def location(self, item):
		return reverse('committee')

class PlayersSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.7

	def items(self):
		return Players.objects.all()

	def location(self, item):
		return reverse('players')


class VideosSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.7

	def items(self):
		return Videos.objects.all()

	def location(self, item):
		return reverse('videos')


class ContactSitemap(Sitemap):

	def items(self):
		return Contact.objects.all()

	def location(self, item):
		return reverse('contact')