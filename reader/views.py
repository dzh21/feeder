from django.views.generic import ListView
from .models import Feed, NewsLine
from django.http import HttpResponse

import re


class FeedView(ListView):
    model = Feed


class NewsLineView(ListView):
    model = NewsLine
    paginate_by = 20

    def get_queryset(self):
        cnt = 1000
        return NewsLine.objects.filter(feed__exact=self.kwargs['pk']).\
            order_by('-published')[:cnt]


def readedall(request):
    if request.is_ajax():
        # feedid from url
        m = re.search(r'/\d+/', request.path)
        feedid = m.group(0)[1:-1]
        news_lines = NewsLine.objects.filter(feed__exact=feedid). \
                                        exclude(readed__exact=True)
        for line in news_lines:
            line.readed = True
            line.save()
        message = "readed all - OK "
    else:
        message = "not ajax:/"

    return HttpResponse(message)


def readed(request):
    if request.is_ajax():
        # mark as readed in database
        # message = "ajax! " + request.POST['newsid']
        line = NewsLine.objects.get(pk=request.POST['newsid'])
        line.readed = True
        line.save()
        message = "readed one - OK"
    else:
        message = "not ajax:/"

    return HttpResponse(message)