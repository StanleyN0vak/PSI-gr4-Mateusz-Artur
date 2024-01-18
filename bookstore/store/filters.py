import django_filters
from .models import Order

"""""
class OrderDetailsFilter(django_filters.FilterSet):
    total_price = django_filters.RangeFilter()

    class Meta:
        model = OrderDetails
        fields = ['total_price']

"""""

class OrderFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(field_name="order_date", lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name="order_date", lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['order_date']

