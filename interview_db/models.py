from django.db import models
from django import forms
from django.forms import ModelForm
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

    full_title = models.CharField(max_length=255)
    major_abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.major_abbreviation
    
    class Meta:
        ordering = ['major_abbreviation',]
        
class Location(models.Model):

    location = models.CharField(max_length=255,
                               )

    def __str__(self):
        return self.location
    
    class Meta:
        ordering = ['location',]

        
class Student(models.Model):  
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    )
    STANDING = (
        ('Fr', 'Freshman'),
        ('So', 'Sophmore'),
        ('Jr', 'Junior'),
        ('Sr', 'Senior'),
        ('Ma', 'Masters'),
        ('Ph', 'PhD')       
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
    artifacts_url = models.URLField(help_text="URL for Google Drive folder where student artifacts are stored.")
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
    standing = models.CharField(choices=STANDING,
                               max_length=2,
                               blank=True)
    major = models.ManyToManyField(Major) 
    intended_major = models.BooleanField(blank=True)                                  
                                 
    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name)
    
    def declared_major(self):
        return ','.join([ major.major_abbreviation for major in self.major.all() ])
        

               
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
                                  null=True,
                                  help_text="Direct URL for transcribed interview, edited for publication.")
	image = models.ImageField(upload_to='interview_db_images', default="", blank=True, null=True)
	image_alt_text = models.CharField(max_length=255, blank=True, null=True, help_text="Describe the image in detail so that a non-sighted user might also get that personal connection.")
	
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
    
    class Meta:
        ordering = ['resource_category',]

class ResourceLink(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255, 
                                help_text="The text used as the link to the resource.")
    description = models.CharField(max_length=5000,
                                        help_text="Provide a <strong>brief</strong> description. Something that could be the title attribute of the link.")
    category = models.ForeignKey(ResourceCategory,on_delete=models.PROTECT, help_text="See our <a href='https://docs.google.com/document/d/1nDEYzdfqIDRQwOEKhRHZiiX8hHj4OxiTlNbYmF4dZUQ/edit?usp=sharing'>category guidelines</> for resource links.")
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title',]
    

class Story(models.Model):
    interview = models.ForeignKey(Interview,on_delete=models.PROTECT)
    story = models.TextField(help_text="Stories should be understandable and interesting all on their own.")
    code = models.ForeignKey(Coding,on_delete=models.PROTECT,
                                help_text="See our <a href='https://docs.google.com/document/d/18el41a2DJ4hdHk-yPVQEDBSzGNb0HO-mlGHp33-nCqE/edit?usp=sharing'>code definitions</>."
                                )
    subcode = models.ForeignKey(SubCode,on_delete=models.PROTECT, 
                                    help_text="See our <a href='https://docs.google.com/document/d/18el41a2DJ4hdHk-yPVQEDBSzGNb0HO-mlGHp33-nCqE/edit?usp=sharing'>sub-code definitions</>."
                                    )
    related_resource_links = models.ManyToManyField(ResourceLink,blank=True,
                                                        help_text="Select any resources that would be useful or relevant in this situation, whether mentioned in the story or not.<br/>"
                                                        )
    story_order_position = models.IntegerField(help_text="Logical position of story within context of other stories w/in interview. <strong>Must be unique</strong> to other stories of the same interview!")

    def __str__(self):
        return str(self.interview) + ": " + str(self.story_order_position)
            
    @property
    def short_story(self):
        return truncatechars(self.story, 150)
        
    class Meta:
        verbose_name_plural = "Stories"
        unique_together = ('interview','story_order_position')
        

