# Generated by Django 3.0 on 2022-08-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20220810_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='limit_book',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]