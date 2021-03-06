from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse_lazy, reverse
from django.utils import timezone 

class Post(models.Model):
    title = models.CharField(max_length=250, default="")

    body = HTMLField(blank=True)
    body_short = models.TextField(blank=True, null=True)

    date_published = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    
    slug = models.CharField(max_length=1000, null=True)

    visible = models.BooleanField(default=True)

    # thumbnail = models.ImageField(upload_to='images', blank=True)
    # caption_url = models.URLField(blank=True)

    # tag = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-date_published']
    
    def date_short(self):
        date = timezone.localtime(self.date_published)
        return date.strftime("%b %-d, %Y")

    def body_trimmed(self):
        br_first_index = self.body.find('</p>')
        if br_first_index != -1:
            return self.body[0:(br_first_index + 4)]
        
        return self.body



    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])
    
    def date_edited_short(self):
        return self.date_edited.strftime("%b %-d, %Y at %-I:%M %p")
        

class Image(models.Model):
    title = models.CharField(max_length=250, default="")
    path = models.ImageField(upload_to='images', blank=True)
