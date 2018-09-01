from django.core.management.base import BaseCommand
from reader.models import NewsLine

import datetime

class Command(BaseCommand):
    help = 'Clear old news'

    def handle(self, *args, **options):
        old_cnt = NewsLine.objects.all().count()
        NewsLine.objects.exclude(published__gt=datetime.datetime.now() -
            datetime.timedelta(weeks=4), readed=True).delete()
        print("Lines deleted count: %d" %
            (old_cnt - NewsLine.objects.all().count()))
