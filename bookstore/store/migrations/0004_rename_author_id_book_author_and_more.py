# Generated by Django 4.2.7 on 2024-01-11 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_author_alias'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publisher_id',
            new_name='publisher',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='address_id',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='client_id',
            new_name='client',
        ),
    ]
