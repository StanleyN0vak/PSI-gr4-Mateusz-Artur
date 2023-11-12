from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)


class OrderDetails(models.Model):
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    total_price = models.DecimalField(10, 2)
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_details_id = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    price = models.DecimalField(10, 2)
    number_of_pages = models.IntegerField()
    status = models.CharField(max_length=50)
    publisher_id = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    genre_id = models.ForeignKey('Genre', on_delete=models.CASCADE)
    author_id = models.ForeignKey('Author', on_delete=models.CASCADE)


class Author(models.Model):
    author_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)


class Opinion(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=200)
    publication_date = models.DateField(auto_now_add=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
