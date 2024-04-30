from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_at']
    readonly_fields = ['slug','created_at']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display =['name','kategori','created_at']
    readonly_fields = ['slug','created_at']
    
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['name','altKategori','created_at']
    readonly_fields = ['slug','created_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['title','owner','slug','id','created_at']
    readonly_fields = ['slug','created_at']





admin.site.register(Comment, CommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubCategoryAdmin)
admin.site.register(Subjects,SubjectsAdmin)