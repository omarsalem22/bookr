from django.contrib import admin
from django.contrib.admin import AdminSite
from.models import *



class BookrAdminSite(AdminSite):

    title_header='Boookr Admin'
    site_header='Booker Adminstration'
    index_title='Bookr site admin'

admin_site=BookrAdminSite(name='bookr')

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Conributor)
admin.site.register(BookConributor)
admin.site.register(Review)
