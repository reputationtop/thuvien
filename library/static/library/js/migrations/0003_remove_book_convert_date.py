# Generated by Django 3.0 on 2022-07-28 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_convert_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='convert_date',
        ),
    ]