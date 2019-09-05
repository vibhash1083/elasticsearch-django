import namegenerator
import datetime
from books.models import *

for i in range(10000):
	author = Author.objects.create(first_name = namegenerator.gen(), last_name = namegenerator.gen(), author_name = namegenerator.gen())
	post = Post.objects.create(title = namegenerator.gen(), authors = author, publishing_date = datetime.datetime.now().date(), isbn = namegenerator.gen())
