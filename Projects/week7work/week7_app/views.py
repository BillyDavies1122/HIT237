from django.shortcuts import render
from week7_app.models import *
from datetime import *
# Create your views here.
def add_publisher(request):
    pub = Publisher(
        name = 'Amazing books.',
        address = '104 good Way',
        city = 'Big City',
        state_province = 'QLD',
        country = 'Australia',
        website = 'N/A'
    )
# At this point, pub is not saved to the database yet!
    pub.save()
# Now it is.
    return render(request, 'change.html')


def add_author(request):
    auth = Author(
        first_name = 'Bill',
        last_name = 'Davies',
        email = 'Bdavies@yahoo.com'
    )
# At this point, auth is not saved to the database yet!
    auth.save()
# Now it is.
    return render(request, 'change2.html')


def add_book(request):
    pub = Publisher.objects.get(name='Amazing books.')
    new_book = Book(
        title = 'Great Book',
        publisher = pub,
        publication_date = datetime.now()
    )
    new_book.save()
# Next section links the many-to-many relationship
    auth = Author.objects.get(first_name='Billy')
    authtwo = Author.objects.get(first_name='Emily')
    new_book.authors.add(auth,authtwo)
    return render(request, 'change3.html')


def upd_book(request):
    Book.objects.filter(title='Billys Book').update(title="greatnameforbook")
    return render(request,'change3.html')

def del_book(request):
    book = Book.objects.get(title="greatnameforbook")
    book.delete()
    return render(request,'change3.html')
