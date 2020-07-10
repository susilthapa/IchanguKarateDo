from django.db import models
import uuid
import os

from django.shortcuts import reverse
from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

from django.core.exceptions import ValidationError


PLAYERS_CATEGORY = (
	('medalist', 'Medalist'),
	('black_belt', 'Black Belt'),
	('player', 'Player')
	)

COMMITTEE_POSITION = (
	('A', 'President'),
	('B', 'Vice President'),
	('C', 'Treasurer'),
	('D', 'Secretary'),
	('E', 'Member'),
	)


def image_file_path(instance, filename):
  """Generate filepath for new image"""
  ext = filename.split('.')[-1]
  filename = f'{uuid.uuid4()}.{ext}'

  if(instance._meta.model.__name__ == 'Home'):
  	return os.path.join('home/', filename)

  elif(instance._meta.model.__name__ == 'Committee'):
  	return os.path.join('committee/', filename)

  elif(instance._meta.model.__name__ == 'EventDetails' or instance._meta.model.__name__ == 'Events'):
  	return os.path.join('events/', filename)

  elif(instance._meta.model.__name__ == 'Players'):
  	return os.path.join('players/', filename)

  elif(instance._meta.model.__name__ == 'ImageSlider'):
  	return os.path.join('imageSlider/', filename)



class Home(models.Model):
	title = models.CharField(max_length=100, blank=True)
	logo = models.ImageField(upload_to=image_file_path, null=True, blank=True, )
	bg_image = models.ImageField('Background Image', upload_to=image_file_path, blank=True)
	about = models.TextField(blank=True)
	about_image = models.ImageField('About Image', upload_to=image_file_path, blank=True)
    
	class Meta:
		verbose_name_plural = 'Home'
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.pk and Home.objects.exists():
			raise ValidationError(f'Not allowed to create multiple Home Information')
		super(Home, self).save(*args, **kwargs)

class Committee(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to=image_file_path)
	position = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'Committee'
		ordering = ['-position']
	def __str__(self):
		return self.name


class Events(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to=image_file_path)
	description = models.TextField()
	date = models.DateField(null=True)
	slug = models.SlugField(default='',
        editable=False, unique=True)

	class Meta:
		verbose_name_plural = 'Events'
		ordering = ['-date']

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Events, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("events", kwargs={'slug': self.slug})

class EventDetails(models.Model):
	event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_details')
	image = models.ImageField(upload_to=image_file_path, blank=True, null=True)
	description = models.TextField(blank=True)

	class Meta:
		verbose_name_plural = 'Event Details'

	def __str__(self):
		return self.description[:15] + '...'



class Players(models.Model):
	name = models.CharField(max_length=255, blank=True)
	image = models.ImageField(upload_to=image_file_path)
	player_type = models.CharField('Player Type',
					 choices=PLAYERS_CATEGORY,
					 max_length=12
					 )
	description = RichTextField(blank=True)
	date = models.DateField(blank=True, null=True)
	
	class Meta:
		verbose_name_plural = 'Players'
		ordering = ['-date']

	def __str__(self):
		return self.name


class Videos(models.Model):
	link = EmbedVideoField('Video Link')
	description = models.TextField('Video Description')

	class Meta:
		verbose_name_plural = 'Videos'

	def __str__(self):
		return self.description[:15] + '...' 


class Contact(models.Model):
	title = models.CharField(max_length=100)
	address = models.CharField(max_length=200, blank=True, null=True)
	phone_one = models.CharField('Phone Number 1', max_length=17, blank=True)
	phone_two = models.CharField('Phone Number 2', max_length=17, blank=True)
	email = models.EmailField('Email Address', max_length=70)
	fb_link = models.URLField('Facebook Link', max_length=200, unique=True, blank=True)
	insta_link = models.URLField('Instagram Link', max_length=200, unique=True, blank=True)
	youtube_link = models.URLField('Youtube Link', max_length=200, unique=True, blank=True)
	

	class Meta:
		verbose_name_plural = 'Contact'

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.pk and Contact.objects.exists():
			raise ValidationError(f'Not allowed to create multiple Contact Information')
		super(Contact, self).save(*args, **kwargs)

class ImageSlider(models.Model):
	image_name = models.CharField(max_length=100)
	image = models.ImageField(upload_to=image_file_path)

	class Meta:
		verbose_name_plural ='ImageSlider'

	def __str__(self):
		return self.image_name

