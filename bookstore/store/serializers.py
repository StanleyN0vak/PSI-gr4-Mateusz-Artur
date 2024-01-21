from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from datetime import date


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class AddressSerializer(serializers.HyperlinkedModelSerializer):
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


class ClientSerializer(serializers.HyperlinkedModelSerializer):
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


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
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

class OpinionSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.SlugRelatedField(slug_field='title', queryset=Book.objects.all())

    class Meta:
        model = Opinion
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):

    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='last_name')
    class Meta:
        model = Order
        fields = '__all__'

