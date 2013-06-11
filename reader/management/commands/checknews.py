from django.core.management.base import BaseCommand
from reader.models import Feed, NewsLine

import feedparser
import datetime
from django.utils import timezone

class Command(BaseCommand):
	help = 'Check news by feeds'

	def handle(self, *args, **options):
		feeds = Feed.objects.all()		
		for feed in feeds:						
			d = feedparser.parse(feed.link)						
			skip_cnt = 0
			for item in d.entries:				
				news_line = NewsLine()
				news_line.feed_id = feed.id
				news_line.link_id = item.id
				news_line.title = item.title
				news_line.published = timezone.make_aware(datetime.datetime(*item.published_parsed[:-3]), timezone.get_current_timezone())
				news_line.summary = item.summary
				try:
					news_line.save()
				except Exception, e:
					#print 'error: %r' % e		
					skip_cnt += 1
			print 'feed %s parsed: add %d, skip %d' % (feed.link, len(d.entries) - skip_cnt, skip_cnt)
				