import django_filters
from .models import OrderDetails

class OrderDetailsFilter(django_filters.FilterSet):
    number = django_filters.RangeFilter()

    class Meta:
        model = OrderDetails
        fields = ['total_price']