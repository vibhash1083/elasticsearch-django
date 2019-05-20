import namegenerator
import datetime
from books.models import *


author = Author.objects.create(first_name = namegenerator.gen(), last_name = namegenerator.gen(), author_name = namegenerator.gen())
book = Book.objects.create(title = namegenerator.gen(), authors = author, )