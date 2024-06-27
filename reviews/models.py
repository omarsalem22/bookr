from django.db import models
from django.contrib import auth

# Create your models here.



class Publisher (models.Model):
    name= models.CharField(max_length=50,help_text='name of publisher')
    website=models.URLField(help_text='The Publisher \'s website ')
    email=models.EmailField(help_text='The Publisher \'s email address . ')


    def __str__(self) :
        return self.name
    


class  Book(models.Model):

    title=models.CharField(max_length=50,help_text='title if the book')
    publication_date=models.DateField(verbose_name='Date of book publication')
    isbn=models.CharField(max_length=20,verbose_name='isbn number of the book')
    publisher=models.ForeignKey(Publisher\
                                ,on_delete=models.CASCADE
                                 )
    contributors=models.ManyToManyField('Conributor',through='BookConributor')
     

    def __str__(self) :
        return self.title

class Conributor(models.Model):
    first_name=models.CharField\
    (max_length=50,verbose_name='Conributor first name')
    last_name=models.CharField\
    (max_length=50,verbose_name='Conributor last name')
    email=models.EmailField\
    (max_length=254,help_text="The Conributor email with the contributor.")

    def __str__(self) :
        return self.first_name
    



class BookConributor(models.Model):
    class  ConributionRole(models.TextChoices):
        AUTHOR="AUTHOR","Author"
        CO_AUTHOR="CO_AUTHOR","Co_Author"
        EDITOR="EDITOR",'Editor'
    book=models.ForeignKey \
        ( Book , on_delete=models.CASCADE)
    contributor= models.ForeignKey \
        (Conributor,on_delete=models.CASCADE)
    
    role=models.CharField\
        (verbose_name="role of contributor for this book",\
        choices=ConributionRole.choices,max_length=20
        )

class Review(models.Model):
    content=models.CharField(max_length=254,help_text='The Review Text')
    rating=models.IntegerField(help_text="rating of reviewer has given")
    date_created=models.DateTimeField(auto_now_add=True,\
                 help_text="The date the review has created")
    
    date_updated=models.DateTimeField\
                 (null=True , \
                  
                  help_text="date of last review edite"
                  
                  )
    creator=models.ForeignKey\
              (auth.get_user_model(),on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,\
                           help_text="The book thst this review for")                                    
    

        



    


    




    