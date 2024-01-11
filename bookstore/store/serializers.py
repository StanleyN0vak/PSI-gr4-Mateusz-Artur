from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from datetime import date


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.country = validated_data.get('country', instance.country)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.street = validated_data.get('street', instance.street)
        instance.house_number = validated_data.get('house_number', instance.house_number)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(slug_field='author_name', queryset=Author.objects.all())

    genre = serializers.SlugRelatedField(slug_field='genre_name', queryset=Genre.objects.all())

    publisher = serializers.SlugRelatedField(slug_field='publisher_name', queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = '__all__'


class OrderDetailsSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(slug_field='title', queryset=Book.objects.all())
    class Meta:
        model = OrderDetails
        fields = '__all__'

    def create(self, validated_data):
        order_details = OrderDetails.objects.create(**validated_data)
        return order_details

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.status = validated_data.get('status', instance.status)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.book = validated_data.get('book', instance.book)
        instance.save()
        return instance

    def validate(self, data):
        # Sprawdź, czy ilość jest większa lub równa 1
        if data['quantity'] < 1:
            raise serializers.ValidationError({
                'quantity': 'Ilość musi być większa lub równa 1.'
            })

        # Sprawdź, czy cena jest dodatnia
        if data['total_price'] <= 0:
            raise serializers.ValidationError({
                'total_price': 'Cena musi być dodatnia.'
            })

        return data

class OrderSerializer(serializers.ModelSerializer):

    order_details = serializers.SlugRelatedField(slug_field='order_number', queryset=OrderDetails.objects.all())

    class Meta:
        model = Order
        fields = '__all__'


class OpinionSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(slug_field='title', queryset=Book.objects.all())

    class Meta:
        model = Opinion
        fields = '__all__'

