from django.urls import path, include
from . import views 

urlpatterns =[
    #Get product price by passing productcode, date and giftCardCode 
    path('get-book/',views.book_search,name="book_search"),

]