from .documents import PostDocument
from django.http import HttpResponse
# from elasticsearch_dsl.query import Q
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

from django.shortcuts import render

# Create your views here.

# def book_search(request):

# 	searchr = PostDocument.search().filter("match", title="baggy")
# 	qs = searchr.to_queryset()
# 	print(qs)
# 	return HttpResponse(qs)


def search(request):

	client = Elasticsearch()

	q = request.GET.get('q')
	if q:
		searchVar = Search().using(client).query("match", title=q)
		response = searchVar.execute()
		# qs = searchVar.to_queryset()
	else:
		searchVar = ''
	
	return render(request, 'search/search.html', {'posts': searchVar})


