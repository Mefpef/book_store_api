import django.forms.fields
from rest_framework import serializers

from .models import Book


class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "authors",
            "published_year",
            "acquired",
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "external_id",
            "title",
            "authors",
            "published_year",
            "acquired",
            "thumbnail",
        ]
