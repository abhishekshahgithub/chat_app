from django.contrib import admin

# Register your models here.

from .models import Chatter

class chatterAdmin(admin.ModelAdmin):
	list_display = ["chat_field", "sender"]
	list_display_links = ["sender"]
	list_filter = ["sender","receiver"]

	# search_fields = ["name"]
	class Meta:
		model = Chatter


admin.site.register(Chatter, chatterAdmin)
