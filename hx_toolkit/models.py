from django.db import models


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
        ('Au', 'Autumn'),
        ('Wi', 'Winter'),
        ('Sp', 'Spring'),
        ('Su', 'Summer')
    )

    title = models.CharField(max_length=255)
    short_body = models.TextField(blank=True,
                                  null=True)
    long_body = models.TextField()
    image = models.ImageField(upload_to='hx_toolkit_images')

    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT)

    slug = models.SlugField(unique=True)

    # data needed for time based card view
    phase = models.CharField(choices=PHASE_CHOICES,
                             max_length=1,
                             blank=True,
                             null=True)
    quarter = models.CharField(choices=QUARTER_CHOICES,
                               max_length=2,
                               blank=True,
                               null=True)
    week = models.IntegerField(blank=True,
                               null=True)
    related_articles = models.ManyToManyField("self",
                                              related_name='related_articles',
                                              blank=True)
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

    def get_article_filename(self):
        return self.slug + ".html"
