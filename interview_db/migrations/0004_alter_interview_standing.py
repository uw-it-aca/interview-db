# Generated by Django 3.2.15 on 2022-08-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_db', '0003_auto_20220803_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='standing',
            field=models.CharField(blank=True, choices=[('Fr', 'Freshman'), ('So', 'Sophomore'), ('Jr', 'Junior'), ('Sr', 'Senior'), ('Al', 'Alumni - undergrad'), ('Ma', 'Masters'), ('Ph', 'PhD')], max_length=2),
        ),
    ]
