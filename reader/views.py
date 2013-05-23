from django.views.generic import ListView
from .models import Feed, NewsLine

class FeedView(ListView):
	model = Feed

class NewsLineView(ListView):
	model = NewsLine		
	paginate_by = 10

	def get_queryset(self):		
		cnt = 1000			
		
		return NewsLine.objects.filter(feed__exact=self.kwargs['pk']).order_by('-published')[:cnt]