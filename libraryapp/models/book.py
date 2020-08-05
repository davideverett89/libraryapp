from django.db import models
from .library import Library
from .librarian import Librarian

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()
    isbn_num = models.IntegerField()
    location = models.ForeignKey(Library, null=True, on_delete=models.CASCADE, default=None)
    librarian = models.ForeignKey(Librarian, null=True, on_delete=models.SET_NULL, default=None)
    

    class Meta:
        verbose_name = ("book")
        verbose_name_plural = ("books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
