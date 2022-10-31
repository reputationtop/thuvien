# Generated by Django 3.0 on 2022-10-30 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='emails_in', to=settings.AUTH_USER_MODEL),
        ),
    ]
