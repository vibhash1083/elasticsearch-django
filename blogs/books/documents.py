# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django_elasticsearch_dsl import Index, fields, Document
# from django_elasticsearch_dsl import DocType
from django_elasticsearch_dsl.registries import registry
from books.models import Author, Post

# Name of the Elasticsearch index
search_index = Index('blogs')
# See Elasticsearch Indices API reference for available settings
search_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

# @search_index.doc_type
@registry.register_document
# @search_index.document
class PostDocument(Document):
    authors = fields.NestedField(properties={
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'author_name': fields.TextField(),
        'pk': fields.IntegerField(),
    }, include_in_root=True)

    # isbn = fields.KeywordField()

    # class Meta:
    class Django:
        model = Post

        fields = [
            'title',
            'publishing_date',
        ]
        related_models = [Author]

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Author):
            return related_instance.post_set.all()
