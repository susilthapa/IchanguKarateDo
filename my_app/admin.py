from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib.auth.models import Group

from .models import (
	Home,
	Committee,
	EventDetails,
	Events, 
	Players,
	ImageSlider,
	Videos,
	Contact,
	)


admin.site.register(Home)

class CommitteeAdmin(admin.ModelAdmin):
	list_display = ('name', 'position')
	search_fields = ('name', 'position')

admin.site.register(Committee, CommitteeAdmin)


class EventDetailsInline(admin.TabularInline):
	model = EventDetails

class EventsAdmin(admin.ModelAdmin):
	inlines = [
		EventDetailsInline
	]

	list_display = ('title', 'date')
	date_hierarchy = 'date'
admin.site.register(Events, EventsAdmin)


class PlayersAdmin(admin.ModelAdmin):
	list_display = ('player_type', 'name', 'image')
	search_fields = ('name', 'player_type')
	list_filter = ('player_type',)
	date_hierarchy = 'date'


admin.site.register(Players, PlayersAdmin)
admin.site.register(ImageSlider)


admin.site.register(Videos)


class ContactAdmin(admin.ModelAdmin):
	list_display = ('title', 'phone_one', 'phone_two', 'email')
admin.site.register(Contact, ContactAdmin)



# Admin page for client

from django.contrib.admin import AdminSite
class IchanguAdminSite(AdminSite):
    site_header = "Ichangu Admin"
    site_title = "Ichangu Karate Do"
    index_title = "Welcome to Ichangu AdminPage"

ichangu_admin_site = IchanguAdminSite(name='ichangu_admin')

ichangu_admin_site.register(Home)
ichangu_admin_site.register(Committee, CommitteeAdmin)
ichangu_admin_site.register(EventDetails)
ichangu_admin_site.register(Events, EventsAdmin)
ichangu_admin_site.register(Players, PlayersAdmin)
ichangu_admin_site.register(ImageSlider)
ichangu_admin_site.register(Videos)
ichangu_admin_site.register(Contact, ContactAdmin)