# Generated by Django 3.0 on 2022-08-21 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20220821_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='recipients',
        ),
        migrations.AddField(
            model_name='email',
            name='recipients',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='emails_received', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='Category_uer',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]