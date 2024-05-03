from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50,verbose_name='Kategori')
    slug = models.SlugField(null = True, blank = True, editable = False)
    content = models.CharField(max_length=200, verbose_name = 'İçerik',null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add = True, null =True, verbose_name="Oluşturulma Tarihi")
        
    def save(self, *args,**kwargs):
        self.slug = slugify(self.name.replace('ı','i'))
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = '01-Kategoriler'
        verbose_name = 'Kategori'
        ordering = ['name']
        
class Subcategory(models.Model):
    name = models.CharField(max_length = 50,verbose_name='Alt Kategori')
    slug = models.SlugField(null = True, blank = True, editable = False)
    kategori = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
    created_at = models.DateTimeField(auto_now_add = True, null =True, verbose_name="Oluşturulma Tarihi")
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.name.replace('ı','i'))
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = '02-Alt Kategoriler'
        verbose_name = 'Alt Kategori'
        ordering = ['name']

class Subjects(models.Model):
    name = models.CharField(max_length= 100,verbose_name='Konu')
    slug = models.SlugField(null = True, blank = True ,editable=False)
    altKategori = models.ForeignKey(Subcategory,on_delete = models.SET_NULL,null = True)
    created_at = models.DateTimeField(auto_now_add = True, null =True, verbose_name="Oluşturulma Tarihi")

    def save(self, *args,**kwargs):
        self.slug = slugify(self.name.replace('ı','i'))
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural= '03-Konu Başlıkları'
        verbose_name = 'Konu'
        ordering = ['name']

class Comment(models.Model):
    id = models.UUIDField(primary_key = True, db_index = True , unique= True , default =uuid.uuid4 , editable = False)
    title = models.CharField(max_length =400,verbose_name = 'Başlık')
    owner = models.ForeignKey(User, on_delete = models.CASCADE,null = True, verbose_name = 'Kullanıcı')
    subjects = models.ForeignKey(Subjects,on_delete=models.SET_NULL, null= True,verbose_name='Konu')
    content =RichTextField(('Yorumunuz'))
    image = models.ImageField(upload_to='forum/', verbose_name='Resim',null=True,blank= True)
    slug = models.SlugField(null = True, blank = True, editable = False)
    created_at = models.DateTimeField(auto_now_add = True, null =True, verbose_name="Oluşturulma Tarihi")
    
    def save(self, *args ,**kwargs):
        self.slug = f"{slugify(self.title.replace('ı','i'))} - {str(self.id)[:8]}"
        self.slug = slugify(self.title.replace('ı','i'))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "04-Yorumlar"
        verbose_name = "Yorum"
        ordering = ['-created_at']
