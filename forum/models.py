from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(null = True, blank = True, editable = False)
    content = models.CharField(max_length=200, verbose_name = 'İçerik',null=True)
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.name.replace('ı','i'))
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategori'
        
class Subcategory(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(null = True, blank = True, editable = False)
    content = models.CharField(max_length=200, verbose_name = 'İçerik',null=True)
    kategori = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.name.replace('ı','i'))
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Alt Kategoriler'
        verbose_name = 'Alt Kategori'

class Comment(models.Model):
    id = models.UUIDField(primary_key = True, db_index = True , unique= True , default =uuid.uuid4 , editable = False)
    title = models.CharField(max_length = 50,verbose_name = 'Başlık')
    owner = models.ForeignKey(User, on_delete = models.CASCADE,null = True, verbose_name = 'Kullanıcı')
    kategori = models.OneToOneField(Category, on_delete = models.SET_NULL, null = True)
    altKategori = models.OneToOneField(Subcategory, verbose_name = 'Alt Kategori', on_delete = models.SET_NULL, null=True)
    content =RichTextField('Yorumunuz')
    image = models.ImageField(upload_to='forum/', verbose_name='Resim',null=True)
    slug = models.SlugField(null = True, blank = True, editable = False)
    created_at = models.DateTimeField(auto_now_add = True, null =True)
    
    def save(self, *args ,**kwargs):
        self.slug = slugify(self.title.replace('ı','i'))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Yorumlar"
        verbose_name = "Yorum"
