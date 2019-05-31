from .documents import PostDocument
from django.http import HttpResponse
from elasticsearch_dsl.query import Q

# Create your views here.

def book_search(request):
	searchr = PostDocument.search().filter("term", title="the")
	qs = searchr.to_queryset()
	print(qs)
	return HttpResponse(qs)

