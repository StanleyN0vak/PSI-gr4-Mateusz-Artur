from django.db import models
import django_filters


class CustomFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter()
    number = django_filters.RangeFilter()


class Address(models.Model):
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return self.country



class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Author(models.Model):
    author_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True, blank=True)


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_pages = models.IntegerField()
    status = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class OrderDetails(models.Model):
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_details = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)


class Opinion(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(null=True)
    publication_date = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
