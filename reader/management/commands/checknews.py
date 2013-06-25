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
			print 'start parsing %s' % feed.link
			d = feedparser.parse(feed.link)						
			skip_cnt = 0
			for item in d.entries:				
				news_line = NewsLine()
				news_line.feed_id = feed.id
				news_line.link_id = item.link
				news_line.title = item.title
				#news_line.published = timezone.make_aware(datetime.datetime(*item.published_parsed[:-3]), timezone.get_current_timezone())
				news_line.published = timezone.make_aware(datetime.datetime(*item.updated_parsed[:-3]), timezone.get_current_timezone())
				news_line.summary = item.summary
				try:
					news_line.save()
				except Exception, e:
					#print 'error: %r' % e		
					skip_cnt += 1
			print 'parsed: add %d, skip %d' % (len(d.entries) - skip_cnt, skip_cnt)
				
