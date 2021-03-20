from django.db import models

# Create your models here.


class Entry(models.Model):
    header = models.CharField(max_length=120)
    detail = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.header


class Author(models.Model):
    name = models.CharField(max_length=120, default=" ")
    surname = models.CharField(max_length=120)

    def __str__(self):
        return self.name + " " + self.surname

