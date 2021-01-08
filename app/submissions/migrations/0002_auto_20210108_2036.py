# Generated by Django 3.1.2 on 2021-01-08 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0003_auto_20210108_2036'),
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assignments.assignment'),
        ),
    ]
