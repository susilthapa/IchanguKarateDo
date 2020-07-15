from django.urls import path
from my_app.views import (
	HomePageView,
	ContactPagView,
	PlayersPageView,
	VideosPageView,
	CommitteePageView,
	EventsPageView,
	EventsDetailPageView,	
)

from my_app.admin import ichangu_admin_site

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('contact/', ContactPagView.as_view(), name='contact'),
	path('gallery/players/', PlayersPageView.as_view(), name='players'),
	path('gallery/videos/', VideosPageView.as_view(), name='videos'),
	path('committee/', CommitteePageView.as_view(), name='committee'),
	path('events/', EventsPageView.as_view(), name='events'),
	path('events/<slug>/', EventsDetailPageView.as_view(), name='events-detail'),
	path('ichangu_9988/', ichangu_admin_site.urls)
]