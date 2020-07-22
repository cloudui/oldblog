from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=250, default="")

    body = HTMLField(blank=True)

    date_published = models.DateTimeField(auto_now_add=True)
    
    slug = models.CharField(max_length=1000, null=True)

    visible = models.BooleanField(default=True)

    thumbnail = models.ImageField(upload_to='images', blank=True)
    caption_url = models.URLField(blank=True)

    tag = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-date_published']
    
    def date_short(self):
        return self.date_published.strftime("%b %d, %Y")

    def body_trimmed(self):
        br_first_index = self.body.find('</p>')
        if br_first_index != -1:
            return self.body[0:(br_first_index + 4)]
        
        return self.body



    
    def __str__(self):
        return self.title
