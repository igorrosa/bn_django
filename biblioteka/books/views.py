from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Book, Author


# Create your views here.
def home(request):
    context = {
        'books': books
    }
    return render(
        request=request,
        context=context,
        template_name="books/home.html"
    )

def books(request):
    context = {
        'books': books
    }
    return render(
        request=request,
        context=context,
        template_name="books/books.html"
    )

def books_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(
        request=request,
        context=context,
        template_name="books/books_list.html"
    )

def authors(request):
    context = {
        'authors': authors
    }
    return render(
        request=request,
        context=context,
        template_name="books/authors.html"
    )

def authors_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
        #'authors trafia do przestrzeni nazw w html a authors jest z authors = book...
    }
    return render(
        request=request,
        context=context,
        template_name="books/authors_list.html"
    )

def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(
        request,
        "books/book_details.html",
        {
            "book": book,
            "version": 1.0,
        }
    )

def loan (request, book_id):
    book = get_object_or_404(Book, pk = book_id)
    if book.is_available:
        book.is_available = False
        book.save()
    else:
        pass
    return HttpResponseRedirect(reverse("books:details", args=(book_id,)))


def loan_back (request, book_id):
    book = get_object_or_404(Book, pk = book_id)
    if not book.is_available:
        book.is_available = True
        book.save()
    else:
        pass
    return HttpResponseRedirect(reverse("books:details", args=(book_id,)))
