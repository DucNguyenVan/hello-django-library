from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Book, Author, Genre, Language, BookInstance
# Register your models here.
@register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'summary', 'isbn', 'display_genre')

@register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Genre)
admin.site.register(Language)

@register(BookInstance)
class AdminBookInstance(admin.ModelAdmin):
    list_display = ('display_book', 'borrower', 'status', 'due_back')