from .models import Home



def base_data(request):
	base = Home.objects.first()
	context = {
		'base': base
	}
	return context
