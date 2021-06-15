from django.shortcuts import render
from .models import Book, BookInstance, Author
from django.views import generic

from catalog import models

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='code')[:5]

class BookDetailView(generic.DetailView):
    model = Book
    