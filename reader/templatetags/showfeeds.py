from reader.models import Feed
from django import template

register = template.Library()

@register.inclusion_tag('reader/reader_feeds.html')
def show_feeds():
	feeds = Feed.objects.all()	
	return { 'feeds': feeds }