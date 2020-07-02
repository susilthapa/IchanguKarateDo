from django.urls import path
from my_app.views import (
	HomePageView,
	ContactPagView,
	GalleryPageView,
	CommitteePageView,
	EventsPageView
)

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('contact/', ContactPagView.as_view(), name='contact'),
	path('gallery/', GalleryPageView.as_view(), name='gallery'),
	path('committe/', CommitteePageView.as_view(), name='committe'),
	path('events/', EventsPageView.as_view(), name='events'),
]