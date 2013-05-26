from django.views.generic import ListView
from .models import Feed, NewsLine
from django.http import HttpResponse

class FeedView(ListView):
	model = Feed

class NewsLineView(ListView):
	model = NewsLine		
	paginate_by = 10

	def get_queryset(self):		
		cnt = 1000			
		
		return NewsLine.objects.filter(feed__exact=self.kwargs['pk']).order_by('-published')[:cnt]

def readed(request):
	if request.is_ajax():
		# mark as readed in database
		# message = "ajax! " + request.POST['newsid']
		news_line = NewsLine.objects.get(pk=request.POST['newsid'])
		news_line.readed = True
		news_line.save()		
	else:
		message = "not ajax:/"

	return HttpResponse('hello')