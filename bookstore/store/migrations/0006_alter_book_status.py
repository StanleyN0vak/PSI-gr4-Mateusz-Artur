# Generated by Django 4.2.7 on 2024-01-11 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_client_owner_order_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('AV', 'Dostępna'), ('UN', 'Niedostępna')], default='AV', max_length=2),
        ),
    ]
