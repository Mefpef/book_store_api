from django.urls import path
from .views import BooksView, BookView, import_data

urlpatterns = [
    path("books/", BooksView.as_view(), name="books"),
    path("books/<int:id>", BookView.as_view(), name="single-book"),
    path("import", import_data, name="import-date"),
]
