# Generated by Django 3.2.25 on 2024-10-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_confirmregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]