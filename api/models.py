from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.TextField()
    title = models.TextField()
    authors = models.JSONField(default=list)
    published_year = models.CharField(max_length=4)
    acquired = models.BooleanField(default=False)
    thumbnail = models.TextField(max_length=450)

    def __str__(self):
        return self.title
