from django.contrib import admin
from .models import Post
from . models import Sidebar

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'image')  # Separate each field with commas
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Sidebar)