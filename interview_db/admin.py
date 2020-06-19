from django.contrib import admin
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.admin.views.main import ChangeList
from .models import StudentType, Major, Location, Student, Interview, Story, Coding, Code, SubCode, ResourceCategory, ResourceLink

from uw_saml.views import LoginView, LogoutView
from uw_saml.utils import is_member_of_group


admin_group = settings.INTERVIEW_DB_AUTHZ_GROUPS['admin']

class SAMLAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return is_member_of_group(request, admin_group)

    def login(self, request, extra_context=None):
        return LoginView.as_view(extra_context=extra_context)(request)

    def logout(self, request, extra_context=None):
        return LogoutView.as_view(extra_context=extra_context)(request)

saml_admin_site = SAMLAdminSite(name='SAMLAdmin')

@admin.register(StudentType, site=saml_admin_site)
class StudentTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
        
@admin.register(Major, site=saml_admin_site)
class MajorAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(Location, site=saml_admin_site)
class LocationAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
        
@admin.register(Student, site=saml_admin_site)
class StudentAdmin (admin.ModelAdmin):    
    fieldsets = (
        (None, {
            'fields': ('first_name','last_name','uw_netid','email')
        }),
        ('Artifacts', {
            'fields': ('artifacts_url',)
        }),
        ('Follow Up', {
            'fields': ('follow_up_consent',)
        }),
    )
    list_display = ('first_name','last_name', 'email','follow_up_consent')
    class Media:
        css = {
            'all': ('css/admin.css',)
        }
    

@admin.register(Interview, site=saml_admin_site)
class InterviewAdmin (admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('student','date'),('interview_quarter','interview_location'))
        }),
        ('Artifacts', {
            'fields': (('image','image_is_not_identifying'),'image_alt_text','interview_notes_url','pull_quote')
        }),
        ('Student Attributes', {
            'fields': (('major','intended_major'),'student_type',('current_year','years_until_graduation'),'standing')
        }),
        ('Permission to Publish', {
            'fields': ('signed_release_form',)
        }),
        ('Publishing Restrictions', {
            'fields': ('no_identifying_photo','no_real_name','no_publishing_stories',('other_publishing_restrictions','other_publishing_restrictions_notes'))
        }),
    )
    list_display = ('date','student', 'declared_major', 'get_followup', 'signed_release_form')
    list_filter = ('major','standing', 'student_type', 'date')
    def get_followup(self,obj):
        return obj.student.follow_up_consent
    get_followup.short_description = 'Follow up'    
    class Media:
        css = {
            'all': ('css/admin.css',)
        }
        
@admin.register(Coding, site=saml_admin_site)
class CodingAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
class CodingInline(admin.StackedInline):
    model = Coding
    extra = 0
        
@admin.register(SubCode, site=saml_admin_site)
class SubCodeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
        
@admin.register(Code, site=saml_admin_site)
class CodeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(Story, site=saml_admin_site)
class StoryAdmin (admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('interview','story')
        }),
        ('Story Metadata', {
            'fields': ('story_order_position',)
        }),
        ('Related Resources', {
            'fields': ('related_resource_links',)
        }),
    )
    inlines = [CodingInline]
    
    class Meta:
        model = Story
        exclude = ['interview']
    list_display = ('get_first_name', 'get_last_name', 'get_date', 'short_story', 'story_order_position')
    list_filter = (
        ('interview', admin.RelatedOnlyFieldListFilter),
        ('code', admin.RelatedOnlyFieldListFilter),
        ('subcode', admin.RelatedOnlyFieldListFilter)
        )
    list_editable = ('story_order_position',)
        
    def get_first_name(self,obj):
        return obj.interview.student.first_name
    get_first_name.short_description = 'First'
    
    def get_last_name(self,obj):
        return obj.interview.student.last_name
    get_last_name.short_description = 'Last'
    
    def get_date(self,obj):
        return obj.interview.date
    get_date.short_description = 'Date'   
    
    class Media:
        css = {
            'all': ('css/admin.css',)
        }


@admin.register(ResourceCategory, site=saml_admin_site)
class ResourceCategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(ResourceLink, site=saml_admin_site)
class ResourceLinkAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}