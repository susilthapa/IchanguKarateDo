from django.db import models
import uuid
import os


def image_file_path(instance, filename):
  """Generate filepath for new image"""
  ext = filename.split('.')[-1]
  filename = f'{uuid.uuid4()}.{ext}'

  if(instance._meta.model.__name__ == 'Home'):
  	return os.path.join('home/', filename)

class Home(models.Model):
	title = models.CharField(max_length=100, blank=True)
	bg_image = models.ImageField('Background Image', upload_to=image_file_path, blank=True)
	about = models.TextField(blank=True)
	about_image = models.ImageField('About Image', upload_to=image_file_path, blank=True)

	class Meta:
		verbose_name_plural = 'Home'
	def __str__(self):
		return self.title


