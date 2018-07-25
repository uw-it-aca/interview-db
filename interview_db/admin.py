from django.contrib import admin
from .models import StudentType, Student, Interview, Story, Coding, SubCode, Article, Category, ResourceLink


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(StudentType)
@admin.register(Student)
class StudentAdmin (admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('first_name','last_name','uw_netid','email')
        }),
        ('Artifacts', {
            'fields': ('image','image_alt_text','artifacts_url')
        }),
        ('Student Attributes', {
            'fields': ('student_type','current_year','year_until_graduation')
        }),
    )
    
admin.site.register(Interview)
admin.site.register(Story)
admin.site.register(Coding)
admin.site.register(SubCode)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ResourceLink)
