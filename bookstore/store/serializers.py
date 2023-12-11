from rest_framework import serializers
from .models import *
from datetime import date


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


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def validate_order_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Data zamówienia nie może być w przyszłości.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validated_data)
        return order

    def update(self, instance, validated_data):

        user = self.context['request'].user
        instance.user = user
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.other_field = validated_data.get('other_field', instance.other_field)
        instance.save()
        return instance


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = '__all__'
