# Generated by Django 3.2.15 on 2022-08-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_db', '0005_auto_20220804_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, choices=[('Getting Help', 'Getting Help'), ('Advice', 'Advice'), ('Working Towards Goals', 'Working Towards Goals'), ('Coming to College', 'Coming to College'), ('Majors', 'Majors'), ('Finding Community', 'Finding Community'), ('Self Reflection', 'Self Reflection'), ('Moving Forward', 'Moving Forward')], max_length=100, null=True)),
                ('codes', models.ManyToManyField(to='interview_db.Code')),
                ('subcodes', models.ManyToManyField(to='interview_db.SubCode')),
            ],
        ),
    ]
