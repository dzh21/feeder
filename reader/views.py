from django.views.generic import ListView
from .models import Feed, NewsLine

class FeedView(ListView):
	model = Feed

class NewsLineView(ListView):
	model = NewsLine

	def get_queryset(self):		
		last_count = 20
		return NewsLine.objects.filter(feed__exact=self.kwargs['pk']).order_by('-published')[:last_count]

