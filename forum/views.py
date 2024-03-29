from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    
    data ={}
    
    for category in categories:
        
        forum = Subcategory.objects.filter(kategori__name = category.name)
        data[category.name] = forum
        
    
        
    print("VERİ:", data)
        
    comments = Comment.objects.filter(owner = request.user)
    context={
        'comments':comments,
        'forumdata': data,
        'categories':categories
    }
    return render(request ,'index.html',context)

def view_404(request, exception):
    return render(request, 'hata.html')

def view_500(request):
    return render(request, 'hata2.html')