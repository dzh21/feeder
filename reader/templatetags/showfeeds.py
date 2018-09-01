from reader.models import Feed, NewsLine
from django import template

register = template.Library()


@register.inclusion_tag('reader/reader_feeds.html')
def show_feeds():
    feeds = Feed.objects.all()
    feeds_with_cnt = []
    for feed in feeds:
        newslines = NewsLine.objects.filter(feed__exact=feed.id). \
            exclude(readed__exact=True)
        feeds_with_cnt.append((newslines.count(), feed))

    return {'feeds': feeds_with_cnt}