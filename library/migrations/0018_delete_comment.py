# Generated by Django 3.0 on 2022-10-27 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_auto_20221027_1810'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]