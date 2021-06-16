from django.shortcuts import render
from .models import Book, BookInstance, Author
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog import models

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 2

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='code')[:5]

class BookDetailView(generic.DetailView):
    model = Book
    
class AuthorListView(generic.ListView):
    model = Author

    def get_queryset(self):
        return Author.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author

class BorrowedBookListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name ='catalog/borrowed_book_list.html'
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)

class AllBorrowedBookListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.can_view_borrowed_books'
    model = BookInstance
    template_name ='catalog/all_borrowed_book_list.html'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o')