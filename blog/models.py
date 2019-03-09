from django.db import models

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()

class Blog(models.Model):
    title=models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    published = PublishedManager()  # Our custom manager.
    class Meta:
        ordering = ('-pub_date',)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title