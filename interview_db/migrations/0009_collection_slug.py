# Generated by Django 3.2.16 on 2023-02-09 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_db', '0008_auto_20230118_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='slug',
            field=models.SlugField(max_length=150, null=True),
        ),
    ]
