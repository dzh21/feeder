from django.contrib import admin
from .models import Feed, NewsLine

admin.site.register(Feed)

class NewsLineAdmin(admin.ModelAdmin):
	list_display = ('published', 'title')

admin.site.register(NewsLine, NewsLineAdmin)