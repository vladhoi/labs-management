# Generated by Django 3.1.2 on 2020-10-16 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0002_auto_20201008_1502'),
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subjects.subject'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
