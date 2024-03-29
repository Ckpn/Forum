from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def index(request):
    categories = Category.objects.all().order_by('name')
    subcategories = Subcategory.objects.all().order_by('name')
    
    context={
        'categories':categories,
        'subcategories':subcategories,
    }
    return render(request ,'index.html',context)

def view_404(request, exception):
    return render(request, 'hata.html')

def view_500(request):
    return render(request, 'hata2.html')

def forum(request):
    mysubcategories= Subcategory.objects.all().order_by('name')
    subjects = Subjects.objects.all().order_by('name')
    context ={
        'mysubcategories' : mysubcategories,
        'subjects' : subjects,
    }
    return render(request, 'forum1.html', context )

def altForum(request):
    mysubjects = Subjects.objects.all().order_by('name')
    comment = Comment.objects.all()
    context={
        'mysubjects': mysubjects,
        'comment':comment,
    }
    return render(request, 'forum2.html', context)


def yorum(request):
    mycomment = Comment.objects.all()
    print(mycomment.id)
    context={
        'mycomment':mycomment
    }
    return render(request, 'forum3.html', context)
    
def create(request):
    form = CommentForm()
    context = {
        'form':form
    }
    return render(request, 'create.html',context)