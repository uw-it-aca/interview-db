from django.contrib import admin
from .models import StudentType, Major, Location, Student, Interview, Story, Coding, SubCode, ResourceCategory, ResourceLink

@admin.register(StudentType)
class StudentTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
        
@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
        
@admin.register(Student)
class StudentAdmin (admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('first_name','last_name','uw_netid','email')
        }),
        ('Artifacts', {
            'fields': ('image','image_alt_text','artifacts_url','follow_up_consent')
        }),
        ('Student Attributes', {
            'fields': ('major','student_type','current_year','year_until_graduation')
        }),
    )
    
admin.site.register(Interview)
admin.site.register(Story)
@admin.register(Coding)
class CodingAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
        
@admin.register(SubCode)
class SubCodeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(ResourceLink)
class ResourceLinkAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
