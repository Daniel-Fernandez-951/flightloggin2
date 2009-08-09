from django.db import models

class NewsItem(models.Model):

    date = models.DateField()
    title = models.CharField(max_length=64)
    text = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-date"]
