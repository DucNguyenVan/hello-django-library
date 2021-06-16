from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('borrowed-books/', views.BorrowedBookListView.as_view(), name='borrowed-books'),
    path('all-borrowed-books/', views.AllBorrowedBookListView.as_view(), name='all-borrowed-books')
]