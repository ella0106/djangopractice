from django.urls import path, include
from .views import HelloAPI, BookAPI,BooksAPI,bookAPI, booksAPI, BookAPIGenerics, BooksAPIGenerics

urlpatterns = [
    path("hello/", HelloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
    path("mixin/books/", BooksAPIGenerics.as_view()),
    path("mixin/book/<int:bid>/", BookAPIGenerics.as_view()),
]