# Generated by Django 3.0 on 2022-08-28 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20220827_0206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='active_all',
            options={'ordering': ['-time_2']},
        ),
        migrations.RemoveField(
            model_name='active_all',
            name='status_notifi',
        ),
        migrations.RemoveField(
            model_name='active_all',
            name='subject',
        ),
        migrations.AddField(
            model_name='active_all',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='library.Category'),
        ),
        migrations.AddField(
            model_name='active_all',
            name='subject_active',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='active_subject', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='active_all',
            name='time_2',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='active_all',
            name='item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='active_listing', to='library.Book'),
        ),
        migrations.AlterField(
            model_name='active_all',
            name='reason',
            field=models.CharField(blank=True, default=None, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='numbe_views',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='dele_listing',
            field=models.BooleanField(default=False),
        ),
    ]
