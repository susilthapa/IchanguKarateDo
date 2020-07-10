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

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('contact/', ContactPagView.as_view(), name='contact'),
	path('gallery/players/', PlayersPageView.as_view(), name='players'),
	path('gallery/videos/', VideosPageView.as_view(), name='videos'),
	path('committe/', CommitteePageView.as_view(), name='committe'),
	path('events/', EventsPageView.as_view(), name='events'),
	path('events/<slug>/', EventsDetailPageView.as_view(), name='events-detail'),

]