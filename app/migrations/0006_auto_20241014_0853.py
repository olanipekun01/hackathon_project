# Generated by Django 3.2.25 on 2024-10-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_programme_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bloodGroup',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='genoType',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='jambNumber',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='primaryEmail',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='studentEmail',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]