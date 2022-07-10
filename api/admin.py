from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['id', 'username', 'email', 'password']
	list_display_links = ['id', 'username']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author', 'content']
	list_display_links = ['id', 'title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'content', 'author', 'post']
	list_display_links = ['id', 'content']