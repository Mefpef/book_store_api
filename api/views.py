import requests
from django.shortcuts import render
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.generics import DestroyAPIView, GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .filters import BookFilter
from django_filters import rest_framework as filters
from .serializers import BooksSerializers, BookSerializer
from django.core.exceptions import ObjectDoesNotExist


class BooksView(ListModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BookView(RetrieveModelMixin, UpdateModelMixin, DestroyAPIView, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        super(BookView, self).delete(request)
        return Response({"message": "object deleted"})


@api_view(["POST"])
def import_data(request):

    if request.method == "POST":
        q = request.data["author"]
        r = requests.get(
            "https://www.googleapis.com/books/v1/volumes?q=inauthor:" + q
        ).json()
        books_data = r["items"]
        books_stack = 0
        for book in books_data:
            external_id = book["id"]
            title = book["volumeInfo"]["title"]

            if "authors" in book["volumeInfo"]:
                authors = [author for author in book["volumeInfo"]["authors"]]
            else:
                authors = "[No Data]"

            published_date = (
                book["volumeInfo"]["publishedDate"]
                if "publishedDate" in book["volumeInfo"]
                else "[No data"
            )
            thumbnail = (
                book["volumeInfo"]["imageLinks"]["thumbnail"]
                if "imageLinks" in book["volumeInfo"]
                else "[No Data]"
            )
            # checking for books to update
            try:
                book_to_update = Book.objects.get(external_id=external_id)
                if book_to_update:
                    book_to_update.external_id = external_id
                    book_to_update.title = title
                    book_to_update.authors = authors
                    book_to_update.published_date = published_date
                    book_to_update.thumbnail = thumbnail
            except ObjectDoesNotExist:
                # creating new book
                new_book = Book(
                    external_id=external_id,
                    title=title,
                    authors=authors,
                    published_year=published_date[:4],
                    thumbnail=thumbnail,
                )
                new_book.save()
                books_stack += 1
        return Response({"imported": books_stack})
