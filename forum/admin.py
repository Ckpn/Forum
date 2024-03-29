from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display =['name']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['title','owner','content','image','slug','created_at']
    readonly_fields = ['slug']





admin.site.register(Comment, CommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubCategoryAdmin)