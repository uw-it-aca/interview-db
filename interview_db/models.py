from django.db import models

class StudentType(models.Model):
    TYPES = (
        ('Commuter', 'Commuter'),
        ('Exchange', 'Exchange'),
        ('First-Gen', 'First-Gen'),
        ('International', 'International'),
        ('LGBTQ', 'LGBTQ'),
        ('Other Minority', 'Minority'),
        ('Transfer', 'Transfer'),
    )  
    
    type = models.CharField(choices=TYPES,
                               max_length=15,
                               unique=True,
                               blank=True,
                               null=True)
    

    def __unicode__(self):
        return self.type

class Student(models.Model):  
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    )  
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    publication_name = models.CharField(max_length=255)
    uw_netID = models.CharField(max_length=10)
    email = models.EmailField(max_length=255,
                                blank=True,
                                null=True)
    artifacts_url = models.URLField()
    gender = models.CharField(choices=GENDER,
                               max_length=1,
                               blank=True,
                               null=True)
    student_type = models.ManyToManyField(StudentType,
                                           blank=True)                                          
    
                                 
    def __unicode__(self):
        return self.last_name
        
               
class Interview(models.Model):
    student = models.ForeignKey(Student,
                                 on_delete=models.PROTECT)

    def __unicode__(self):
        return self.title
        
class Story(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
        
class Coding(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class SubCode(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
        


class ResourceLink(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Article(models.Model):
    PHASE_CHOICES = (
        ('A', 'Phase A'),
        ('B', 'Phase B'),
        ('C', 'Phase C'),
    )
    QUARTER_CHOICES = (
        ('autumn', 'Autumn'),
        ('winter', 'Winter'),
        ('spring', 'Spring'),
        ('summer', 'Summer')
    )

    title = models.CharField(max_length=255)
    short_body = models.TextField(blank=True,
                                  null=True)
    long_body = models.TextField()

    image = models.ImageField(upload_to='interview_db_images')
    image_credit = models.TextField(blank=True,
                                    null=True)
    image_alt_text = models.TextField(blank=True,
                                      null=True)

    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT)

    slug = models.SlugField(unique=True)

    # data needed for time based card view
    phase = models.CharField(choices=PHASE_CHOICES,
                             max_length=1,
                             blank=True,
                             null=True)
    quarter = models.CharField(choices=QUARTER_CHOICES,
                               max_length=6,
                               blank=True,
                               null=True)

    # range btwn -2 and 14 weeks
    week = models.IntegerField(blank=True,
                               null=True)
    related_articles = models.ManyToManyField("self",
                                              related_name='related_article',
                                              blank=True,
                                              symmetrical=False)
    related_links = models.ManyToManyField(ResourceLink,
                                           blank=True)

    def __unicode__(self):
        return self.title

    def article_title_data(self):
        data = {
            'title': self.title,
            'slug': self.slug
        }
        return data

    def get_article_filename(self, is_short=False):
        return self.slug + ".html"
