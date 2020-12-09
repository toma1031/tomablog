from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField("Title", max_length=200)
  image = models.ImageField(upload_to='images', verbose_name='image', null=True, blank=True)
  content = models.TextField("Contents")
  created = models.DateTimeField("Date", default=timezone.now)

  def __str__(self):
    return self.title
