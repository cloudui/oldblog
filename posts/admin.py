from django.contrib import admin

# Register your models here.
from .models import Post, Image

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)