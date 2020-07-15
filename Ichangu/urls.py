

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from my_app.sitemaps import (
	EventsSitemap, 
	ContactSitemap,
	HomeSitemap,
	CommitteeSitemap,
	PlayersSitemap,
	VideosSitemap
	)

from django.contrib.sitemaps.views import sitemap

sitemaps = {
	'home': HomeSitemap,
	'events': EventsSitemap,
	'committee': CommitteeSitemap,
	'players': PlayersSitemap,
	'videos': VideosSitemap,
	'contact': ContactSitemap
}

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('surzero9988/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('', include('my_app.urls'))
]

custom_404 = 'my_app.views.error_404_view'
custom_500 = 'my_app.views.error_500_view'

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
