# Generated by Django 4.2.7 on 2024-01-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_opinion_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='alias',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
