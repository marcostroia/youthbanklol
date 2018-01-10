from django.contrib import admin
from .models import PostModel


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'text','slug','image1']

admin.site.register(PostModel, PostModelAdmin)
