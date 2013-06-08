from reader.models import Feed, NewsLine
from django import template

register = template.Library()

@register.inclusion_tag('reader/reader_feeds.html')
def show_feeds():
	feeds = Feed.objects.all()	
	news_cnt = {}
	for cnt, feed in enumerate(feeds):
		newslines = NewsLine.objects.filter(feed__exact=feed.id).exclude(readed__exact=True)
		news_cnt[cnt] = newslines.count()
	return { 'feeds': feeds, 'news_cnt': news_cnt}