from django.db import models
from django import forms
from django.template.defaultfilters import truncatechars


class StudentType(models.Model):
    TYPE = (
        ('Commuter', 'Commuter'),
        ('Exchange', 'Exchange'),
        ('First-Gen', 'First-Gen'),
        ('International', 'International'),
        ('LGBTQ', 'LGBTQ'),
        ('Other Minority', 'Minority'),
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

    major = models.CharField(max_length=255,
                               )

    def __str__(self):
        return self.major
        
class Location(models.Model):

    location = models.CharField(max_length=255,
                               )

    def __str__(self):
        return self.location

        
class Student(models.Model):  
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
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
    YEAR_LEFT = (
        ('< 1', '< 1'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6')      
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    uw_netid = models.CharField(max_length=10)
    email = models.EmailField(max_length=255,
                                blank=True,
                                null=True)
                                
    image = models.ImageField(upload_to='interview_db_images', default="", blank=True, null=True)
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    artifacts_url = models.URLField()
    follow_up_consent = models.BooleanField()
    
    gender = models.CharField(choices=GENDER,
                               max_length=1,
                               blank=True,
                               null=True)
    student_type = models.ManyToManyField(StudentType,
                                           blank=True)  
                                           
    current_year = models.CharField(choices=YEAR,
                               max_length=1,
                               blank=True)
    year_until_graduation = models.CharField(choices=YEAR_LEFT,
                               max_length=2,
                               blank=True)
    major = models.ManyToManyField(Major)                                   
                                 
    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name)

               
class Interview(models.Model):
	QUARTER = (
		('au', 'Autumn'),
		('wi', 'Winter'),
		('sp', 'Spring'),
		('su', 'Summer')
    )
    
	student = models.ForeignKey(Student,on_delete=models.PROTECT)
	date= models.DateField()
	interview_quarter = models.CharField(choices=QUARTER,max_length=2)
	interview_location = models.ManyToManyField(Location,
                                           blank=True)
	release_form = models.BooleanField()
	release_conditions = models.TextField(blank=True,
                                  null=True)
	interview_notes_url = models.URLField(blank=True,
                                  null=True)
	    
	def __str__(self):
	    return str(self.student) + ": " + str(self.date)
        
class Coding(models.Model):
    code = models.CharField(max_length=500)
    definition = models.CharField(max_length=5000)

    def __str__(self):
        return self.code

class SubCode(models.Model):
    subcode = models.CharField(max_length=255)
    definition = models.CharField(max_length=5000)

    def __str__(self):
        return self.subcode

class ResourceCategory(models.Model):
    resource_category = models.CharField(max_length=500)
    definition = models.CharField(max_length=5000)

    def __str__(self):
        return self.resource_category

class ResourceLink(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    category = models.ForeignKey(ResourceCategory,on_delete=models.PROTECT)
    

    def __str__(self):
        return self.title

class Story(models.Model):
    interview = models.ForeignKey(Interview,on_delete=models.PROTECT)
    story = models.TextField()
    code = models.ForeignKey(Coding,on_delete=models.PROTECT)
    subcode = models.ForeignKey(SubCode,on_delete=models.PROTECT)
    related_resource_links = models.ManyToManyField(ResourceLink,blank=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def short_story(self):
        return truncatechars(self.story, 150)

