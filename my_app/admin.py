from django.contrib import admin

from django.contrib.auth.models import Group

from .models import (
	Home,
	Committee,
	EventDetails,
	Events, 
	Players,
	Videos,
	Contact
	)

admin.site.unregister(Group)

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
admin.site.register(Events, EventsAdmin)


class PlayersAdmin(admin.ModelAdmin):
	list_display = ('name', 'player_type')
	search_fields = ('name', 'player_type')
admin.site.register(Players, PlayersAdmin)


admin.site.register(Videos)


class ContactAdmin(admin.ModelAdmin):
	list_display = ('title', 'phone_one', 'phone_two', 'email')
admin.site.register(Contact, ContactAdmin)

