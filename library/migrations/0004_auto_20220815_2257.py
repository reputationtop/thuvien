# Generated by Django 3.0 on 2022-08-15 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_user_limit_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='limit_book',
            field=models.IntegerField(blank=True, default=7),
        ),
    ]