from django_filters import rest_framework as filters
from django.db import models
from .models import Book


class BookFilter(filters.FilterSet):
    date_from = filters.NumberFilter(field_name="published_year", lookup_expr="gte")
    date_to = filters.NumberFilter(field_name="published_year", lookup_expr="lte")

    class Meta:
        model = Book
        fields = ["authors", "acquired"]
        filter_overrides = {
            models.JSONField: {
                "filter_class": filters.CharFilter,
                "extra": lambda f: {
                    "lookup_expr": "icontains",
                },
            }
        }
