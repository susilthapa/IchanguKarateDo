from django.urls import path
from my_app.views import (
	HomePageView,
	ContactPagView,
	GalleryPageView,
	CommittePageView
)

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('contact/', ContactPagView.as_view(), name='contact'),
	path('gallery/', GalleryPageView.as_view(), name='gallery'),
	path('committe/', CommittePageView.as_view(), name='committe'),
]