from django.urls import path
from . import views
app_name = "books"

urlpatterns = [
    #path("", views.home, ),
    # ex: /books/
    path("books_list", views.books_list, name="books_list"),
    path("books", views.books, name="books"),
    path("books/<int:book_id>", views.book_details, name="details"),
    path("authors_list", views.authors_list, name="authors_list"),
    path("authors", views.authors, name="authors"),
    path("<int:book_id>/loan", views.loan, name="loan"),
    path("/<int:book_id>/loan_back", views.loan_back, name="loan_back"),
]