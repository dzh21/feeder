from django.db import models


class Feed(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=255)

    def __unicode__(self):
        return self.name


class NewsLine(models.Model):
    feed = models.ForeignKey(Feed)
    published = models.DateTimeField()
    title = models.CharField(max_length=255)
    summary = models.TextField()
    link_id = models.CharField(max_length=255)
    readed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('feed', 'link_id')

    def __unicode__(self):
        return self.title