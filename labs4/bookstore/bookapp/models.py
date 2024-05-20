from django.db import models


# Create your models here.

class PublicationHouse(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    year_established = models.IntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name


class Book(models.Model):
    BOOK_CATEGORIES = [
        ("Romance", "Romance"),
        ("Thriller", "Thriller"),
        ("Biography", "Biography"),
        ("Classic", "Classic"),
        ("Drama", "Drama"),
        ("History", "History"),
    ]

    BOOK_COVER = [
        ("Soft", "Soft"),
        ("Hard", "Hard"),
    ]

    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    isbn = models.CharField(max_length=30)
    publishing_year = models.IntegerField()
    pages = models.IntegerField()
    size = models.IntegerField()
    price = models.IntegerField()
    category = models.CharField(max_length=30, choices=BOOK_CATEGORIES)
    cover = models.CharField(max_length=30, choices=BOOK_COVER)
    house = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
