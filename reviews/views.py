from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import Book,Review
from .utils import average_rating

# Create your views here.


def index (request):
   myname="omar salem"
   return render (request,'base.html',{'name':myname})


def list_books(request):
   books=Book.objects.all()
   book_list=[]
   for book in books:
      reviews=book.review_set.all()
      if reviews:
         book_rating= average_rating([review.rating for review in reviews])
         number_of_reviews=len(reviews)
      else:
         book_rating= None
         number_of_reviews=0
      book_list.append({'book':book,\
                           'book_rating':book_rating,\
                           'number_of_reviews':number_of_reviews
                           })   
         
      context={
      'book_list':book_list
     
       }
      

   return render(request,'book_list.html',context)
   
   


def book_detail(request,id):
   
   book=get_object_or_404(Book,id=id)

   reviews=book.review_set.all()


   if reviews:
        reviews=book.review_set.all()
        book_rating= average_rating([review.rating for review in reviews])
        number_of_reviews=len(reviews)
      
   else:
       book_rating= None
       number_of_reviews=0

   my_book=({'book':book,\
      'book_rating':book_rating,\
      'number_of_reviews':number_of_reviews
      })  
   
   context={"book":my_book}


   return render(request,'book_detail.html',context)

