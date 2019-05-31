from django.contrib import admin
from .models import Author, Post

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'author_name', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', )