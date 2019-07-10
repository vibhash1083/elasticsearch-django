from django.contrib import admin
from .models import Author, Post
from .documents import PostDocument

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'author_name', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        q = request.GET.get('q')
        queryset = Post.objects.all()
        if q:
            searchr = PostDocument.search().filter("term", title=q)
            queryset = searchr.to_queryset()
        return queryset

    search_fields = ('title', )