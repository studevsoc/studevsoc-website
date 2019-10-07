from django.contrib import admin

from .models import Post, Comment, Tag, BlogType


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'feature', 'slider', 'created_on',)
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug':('title',)}

class BlogTypeAdmin(admin.ModelAdmin):
    fields =['name']



admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(BlogType)
