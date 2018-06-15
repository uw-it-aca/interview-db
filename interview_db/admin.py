from django.contrib import admin
from .models import Student, StudentType, Interview, Story, Coding, SubCode, Article, Category, ResourceLink


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Student)
admin.site.register(Interview)
admin.site.register(Story)
admin.site.register(Coding)
admin.site.register(SubCode)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ResourceLink)
