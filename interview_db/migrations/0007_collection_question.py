# Generated by Django 3.2.15 on 2022-08-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_db', '0006_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='question',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]