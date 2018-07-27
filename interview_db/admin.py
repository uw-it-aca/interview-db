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
            'fields': ('major','student_type','current_year','year_until_graduation','standing')
        }),
    )
    list_display = ('last_name','first_name', 'declared_major', 'email','follow_up_consent')
    list_filter = ('major',)
    
@admin.register(Interview)
class InterviewAdmin (admin.ModelAdmin):
    list_display = ('date','student', 'get_followup', 'release_form')
    list_filter = ('student','date')
    
    def get_followup(self,obj):
        return obj.student.follow_up_consent
    get_followup.short_description = 'Follow up'
    

@admin.register(Story)
class StoryAdmin (admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'get_date', 'short_story','code','subcode')
    list_filter = ('code','subcode')
    
    def get_first_name(self,obj):
        return obj.interview.student.first_name
    get_first_name.short_description = 'First'
    
    def get_last_name(self,obj):
        return obj.interview.student.last_name
    get_last_name.short_description = 'Last'
    
    def get_date(self,obj):
        return obj.interview.date
    get_date.short_description = 'Date'


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
