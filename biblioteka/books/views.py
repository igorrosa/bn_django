from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core import serializers
from books.forms import AuthorForm
from .models import Book, Author
import json

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
    if 'q' in request.GET: #tworzenie filtrów query i querysety
        query = request.GET.get('q')
        books = books.filter(title__icontains=query)
    if "format" in request.GET:
        format = request.GET.get("format")
        if format == "json":
            data = serializers.serialize('json', books)
            return JsonResponse(json.loads(data), safe=False)

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
    if request.method == "POST":
        if 'loan' in request.POST: #ogarnąć metody
            messages.add_message(request, messages.SUCCESS, "Książkę wypożyczono") # messages z biblioteki django
            book.is_available = False
        elif 'loan_back' in request.POST:
            messages.add_message(request, messages.INFO, "Książkę zwrócono")
            book.is_available = True
    return render(
        request,
        "books/book_details.html",
        {
            "book": book,
            "version": 1.0,
        })
    '''
    book = get_object_or_404(Book, pk=book_id)
    return render(
        request,
        "books/book_details.html",
        {
            "book": book,
            "version": 1.0,
        }
    )'''

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

def author_form_test(request):
    form = AuthorForm()
    return render(
        request,
        "accounts/login.html",
        context={"form": form}
    )