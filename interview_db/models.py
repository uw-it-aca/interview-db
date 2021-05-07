# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.db import models
from django import forms
from django.forms import ModelForm
from django.template.defaultfilters import truncatechars
from django.urls import reverse


class StudentType(models.Model):
    TYPE = (
        ('Commuter', 'Commuter'),
        ('Exchange', 'Exchange'),
        ('First-Gen', 'First-Gen'),
        ('International', 'International'),
        ('LGBTQ', 'LGBTQ'),
        ('Transfer', 'Transfer'),
    )

    type = models.CharField(choices=TYPE,
                            max_length=100,
                            blank=True,
                            null=True
                            )

    def __str__(self):
        return self.type


class Major(models.Model):

    full_title = models.CharField(max_length=255)
    major_abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.major_abbreviation

    class Meta:
        ordering = ['major_abbreviation', ]


class Location(models.Model):

    location = models.CharField(max_length=255,
                                )

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location', ]


class Student(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    uw_netid = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=255,
                              blank=True,
                              null=True)
    artifacts_url = models.URLField(
        help_text="URL for Google Drive folder where student artifacts are stored.")
    follow_up_consent = models.BooleanField()

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

    class Meta:
        ordering = ['first_name', ]


class Interview(models.Model):
    YEAR_LEFT = (
        ('< 1', '< 1'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6')
    )
    YEAR = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8')
    )
    STANDING = (
        ('Fr', 'Freshman'),
        ('So', 'Sophmore'),
        ('Jr', 'Junior'),
        ('Sr', 'Senior'),
        ('Al', 'Alumni - undergrad'),
        ('Ma', 'Masters'),
        ('Ph', 'PhD')
    )
    QUARTER = (
        ('au', 'Autumn'),
        ('wi', 'Winter'),
        ('sp', 'Spring'),
        ('su', 'Summer')
    )

    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    date = models.DateField()
    interview_quarter = models.CharField(choices=QUARTER, max_length=2)
    interview_location = models.ManyToManyField(Location,
                                                blank=True)
    signed_release_form = models.BooleanField()
    pull_quote = models.TextField(
        max_length=200, help_text="A brief, 200 character or less, quote from interview that will engage people.")
    interview_notes_url = models.URLField(blank=True,
                                          null=True,
                                          help_text="Direct URL for transcribed interview, edited for publication.")
    image = models.ImageField(upload_to='interview_db_images', default="", blank=True, null=True,
                              help_text="Image should be 1875 x 2882 (any orientation), saved as an optimized High Quality (60) JPEG.")
    image_is_not_identifying = models.BooleanField(
        help_text="This image doesn't include the student's face.")
    image_alt_text = models.CharField(max_length=255, blank=True, null=True,
                                      help_text="Describe the image in detail so that a non-sighted user might also get that personal connection.")
    intended_major = models.BooleanField(blank=True)
    major = models.ManyToManyField(Major)
    standing = models.CharField(choices=STANDING,
                                max_length=2,
                                blank=True)
    years_until_graduation = models.CharField(choices=YEAR_LEFT,
                                              max_length=3,
                                              blank=True)
    current_year = models.CharField(choices=YEAR,
                                    max_length=1,
                                    blank=True)
    student_type = models.ManyToManyField(StudentType,
                                          blank=True)
    no_identifying_photo = models.BooleanField(
        help_text="No photo of face can be published.")
    no_real_name = models.BooleanField(help_text="Cannot publish real name.")
    no_publishing_stories = models.BooleanField(
        help_text="Stories and artifacts can only be used internally for research.")
    other_publishing_restrictions = models.BooleanField(
        help_text="They had other restrictions on the use of their data.")
    other_publishing_restrictions_notes = models.TextField(
        blank=True, null=True)

    def __str__(self):
        return str(self.student) + ": " + str(self.date)
    class Meta:
        ordering = ['student','-date']
        
    def declared_major(self):
        return ','.join([ major.major_abbreviation for major in self.major.all() ])

    def get_absolute_url(self):
        return reverse('interview_db:interview', args=(), kwargs={'interview_id': str(self.id)})   

class ResourceCategory(models.Model):
    resource_category = models.CharField(max_length=500)
    definition = models.CharField(max_length=5000)

    def __str__(self):
        return self.resource_category
    
    class Meta:
        ordering = ['resource_category',]

class ResourceLink(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255, 
                                help_text="The text used as the link to the resource.")
    description = models.CharField(max_length=5000,
                                        help_text="Provide a <strong>brief</strong> description. Something that could be the title attribute of the link.")
    category = models.ForeignKey(ResourceCategory,on_delete=models.PROTECT, help_text="See our <a href='https://docs.google.com/document/d/1nDEYzdfqIDRQwOEKhRHZiiX8hHj4OxiTlNbYmF4dZUQ/edit?usp=sharing'>category guidelines</a> for resource links.")
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title',]
    
class SubCode(models.Model):
    subcode = models.CharField(max_length=255)
    definition = models.CharField(max_length=5000)
    
    class Meta:
        ordering = ['subcode',] 
        
    def __str__(self):
        return self.subcode

class Code(models.Model):
    topic = models.CharField(max_length=20)
    code = models.CharField(max_length=255)
    definition = models.TextField(max_length=5000)
    
    class Meta:
        ordering = ['topic','code'] 

    def __str__(self):
        return str(self.topic) + " - " + str(self.code)
    
    def get_absolute_url(self):
            return reverse('interview_db:code', args=(), kwargs={'code_id': str(self.id)}) 
        
class Story(models.Model):
    interview = models.ForeignKey(Interview,on_delete=models.PROTECT)
    story = models.TextField(help_text="Stories should be understandable and interesting all on their own.")
    related_resource_links = models.ManyToManyField(ResourceLink,blank=True,
                                                        help_text="Select any resources that would be useful or relevant in this situation, whether mentioned in the story or not.<br/>"
                                                        )
    story_order_position = models.IntegerField(help_text="Logical position of story within context of other stories w/in interview. <strong>Must be unique</strong> to other stories of the same interview!")
    code = models.ManyToManyField(Code, through='Coding')
    subcode = models.ManyToManyField(SubCode, through='Coding')

    def __str__(self):
        return str(self.interview) + ": " + str(self.story_order_position)
            
    @property
    def short_story(self):
        return truncatechars(self.story, 150)
        
    class Meta:
        verbose_name_plural = "Stories"
        unique_together = ('interview','story_order_position')
        ordering = ['story_order_position']
        
class Coding(models.Model):
    code = models.ForeignKey(Code,on_delete=models.PROTECT, 
                                    help_text="See our <a href='https://docs.google.com/document/d/18el41a2DJ4hdHk-yPVQEDBSzGNb0HO-mlGHp33-nCqE/edit?usp=sharing'>code definitions</a>."
                                    )
    subcode = models.ForeignKey(SubCode,on_delete=models.PROTECT,)

    story = models.ForeignKey(Story, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.code) + " > " + str(self.subcode)
    
    class Meta:
        ordering = ['code',] 


