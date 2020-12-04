# Generated by Django 3.1.2 on 2020-10-08 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("subjects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="description",
            field=models.TextField(default="description"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.user",
            ),
            preserve_default=False,
        ),
    ]
