from django.urls import path 
from .views import  index ,list_books,book_detail
urlpatterns = [
    path ("index",index,name="index"),
    path ("list_books",list_books,name="list_books"),
    path ("book_detail/<int:id>",book_detail,name="book_detail"),


    
]
