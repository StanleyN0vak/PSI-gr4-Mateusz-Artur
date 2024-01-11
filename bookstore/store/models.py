from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey


class Address(models.Model):
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return self.city + ' ' + ' ' + self.street + ' '+self.house_number



class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name + ' '+ self.last_name


class Author(models.Model):
    author_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.author_name + ' ' + self.author_last_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)


    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    AVAILABLE = 'AV'
    UNAVAILABLE = 'UN'
    STATUS_CHOICES = [
        (AVAILABLE, 'Dostępna'),
        (UNAVAILABLE, 'Niedostępna'),
    ]
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_pages = models.IntegerField()
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=AVAILABLE,
    )
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class OrderDetails(models.Model):
    PENDING = 'PD'
    COMPLETED = 'CD'
    SHIPPED = 'SD'
    STATUS_CHOICES = [
        (PENDING, 'W trakcie'),
        (COMPLETED, 'Dostarczono'),
        (SHIPPED, "Wysłano")
    ]
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_number = models.IntegerField(null=True)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_details = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Opinion(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(null=True)
    publication_date = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
