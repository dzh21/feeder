from django.conf.urls import patterns, url
from reader import views

urlpatterns = patterns('',
    url(r'^$', views.FeedView.as_view()),
    url(r'^feeds/(?P<pk>\d+)/page(?P<page>\d+)?$',
        views.NewsLineView.as_view(), name='feed_news'),
    url(r'^feeds/\d+/readed$', views.readed),
    url(r'^feeds/\d+/readedall$', views.readedall),
)
