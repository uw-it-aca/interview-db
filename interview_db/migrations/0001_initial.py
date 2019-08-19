# Generated by Django 2.0.13 on 2019-05-07 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=255)),
                ('definition', models.TextField(max_length=5000)),
            ],
            options={
                'ordering': ['topic', 'code'],
            },
        ),
        migrations.CreateModel(
            name='Coding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.ForeignKey(help_text="See our <a href='https://docs.google.com/document/d/18el41a2DJ4hdHk-yPVQEDBSzGNb0HO-mlGHp33-nCqE/edit?usp=sharing'>code definitions</a>.", on_delete=django.db.models.deletion.PROTECT, to='interview_db.Code')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('interview_quarter', models.CharField(choices=[('au', 'Autumn'), ('wi', 'Winter'), ('sp', 'Spring'), ('su', 'Summer')], max_length=2)),
                ('signed_release_form', models.BooleanField()),
                ('pull_quote', models.TextField(help_text='A brief, 200 character or less, quote from interview that will engage people.', max_length=200)),
                ('interview_notes_url', models.URLField(blank=True, help_text='Direct URL for transcribed interview, edited for publication.', null=True)),
                ('image', models.ImageField(blank=True, default='', help_text='Image should be 1875 x 2882 (any orientation), saved as an optimized High Quality (60) JPEG.', null=True, upload_to='interview_db_images')),
                ('image_is_not_identifying', models.BooleanField(help_text="This image doesn't include the student's face.")),
                ('image_alt_text', models.CharField(blank=True, help_text='Describe the image in detail so that a non-sighted user might also get that personal connection.', max_length=255, null=True)),
                ('intended_major', models.BooleanField()),
                ('standing', models.CharField(blank=True, choices=[('Fr', 'Freshman'), ('So', 'Sophmore'), ('Jr', 'Junior'), ('Sr', 'Senior'), ('Al', 'Alumni - undergrad'), ('Ma', 'Masters'), ('Ph', 'PhD')], max_length=2)),
                ('years_until_graduation', models.CharField(blank=True, choices=[('< 1', '< 1'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=3)),
                ('current_year', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=1)),
                ('no_identifying_photo', models.BooleanField(help_text='No photo of face can be published.')),
                ('no_real_name', models.BooleanField(help_text='Cannot publish real name.')),
                ('no_publishing_stories', models.BooleanField(help_text='Stories and artifacts can only be used internally for research.')),
                ('other_publishing_restrictions', models.BooleanField(help_text='They had other restrictions on the use of their data.')),
                ('other_publishing_restrictions_notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['student', '-date'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['location'],
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_title', models.CharField(max_length=255)),
                ('major_abbreviation', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['major_abbreviation'],
            },
        ),
        migrations.CreateModel(
            name='ResourceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_category', models.CharField(max_length=500)),
                ('definition', models.CharField(max_length=5000)),
            ],
            options={
                'ordering': ['resource_category'],
            },
        ),
        migrations.CreateModel(
            name='ResourceLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(help_text='The text used as the link to the resource.', max_length=255)),
                ('description', models.CharField(help_text='Provide a <strong>brief</strong> description. Something that could be the title attribute of the link.', max_length=5000)),
                ('category', models.ForeignKey(help_text="See our <a href='https://docs.google.com/document/d/1nDEYzdfqIDRQwOEKhRHZiiX8hHj4OxiTlNbYmF4dZUQ/edit?usp=sharing'>category guidelines</a> for resource links.", on_delete=django.db.models.deletion.PROTECT, to='interview_db.ResourceCategory')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.TextField(help_text='Stories should be understandable and interesting all on their own.')),
                ('story_order_position', models.IntegerField(help_text='Logical position of story within context of other stories w/in interview. <strong>Must be unique</strong> to other stories of the same interview!')),
                ('code', models.ManyToManyField(through='interview_db.Coding', to='interview_db.Code')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='interview_db.Interview')),
                ('related_resource_links', models.ManyToManyField(blank=True, help_text='Select any resources that would be useful or relevant in this situation, whether mentioned in the story or not.<br/>', to='interview_db.ResourceLink')),
            ],
            options={
                'verbose_name_plural': 'Stories',
                'ordering': ['story_order_position'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('uw_netid', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('artifacts_url', models.URLField(help_text='URL for Google Drive folder where student artifacts are stored.')),
                ('follow_up_consent', models.BooleanField()),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='StudentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('Commuter', 'Commuter'), ('Exchange', 'Exchange'), ('First-Gen', 'First-Gen'), ('International', 'International'), ('LGBTQ', 'LGBTQ'), ('Transfer', 'Transfer')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcode', models.CharField(max_length=255)),
                ('definition', models.CharField(max_length=5000)),
            ],
            options={
                'ordering': ['subcode'],
            },
        ),
        migrations.AddField(
            model_name='story',
            name='subcode',
            field=models.ManyToManyField(through='interview_db.Coding', to='interview_db.SubCode'),
        ),
        migrations.AddField(
            model_name='interview',
            name='interview_location',
            field=models.ManyToManyField(blank=True, to='interview_db.Location'),
        ),
        migrations.AddField(
            model_name='interview',
            name='major',
            field=models.ManyToManyField(to='interview_db.Major'),
        ),
        migrations.AddField(
            model_name='interview',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='interview_db.Student'),
        ),
        migrations.AddField(
            model_name='interview',
            name='student_type',
            field=models.ManyToManyField(blank=True, to='interview_db.StudentType'),
        ),
        migrations.AddField(
            model_name='coding',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='interview_db.Story'),
        ),
        migrations.AddField(
            model_name='coding',
            name='subcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='interview_db.SubCode'),
        ),
        migrations.AlterUniqueTogether(
            name='story',
            unique_together={('interview', 'story_order_position')},
        ),
    ]
