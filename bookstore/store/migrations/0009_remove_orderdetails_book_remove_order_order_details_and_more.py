# Generated by Django 4.2.7 on 2024-01-18 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_orderdetails_status_order1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='book',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_details',
        ),
        migrations.RemoveField(
            model_name='order',
            name='owner',
        ),
        migrations.AddField(
            model_name='order',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.book'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PG', 'Kompletowane'), ('CD', 'Dostarczono'), ('SD', 'Wysłano')], default='PG', max_length=3),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='Order1',
        ),
        migrations.DeleteModel(
            name='OrderDetails',
        ),
    ]
