from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name = 'index'),
    path('forum/',forum, name='forum'),
    path('altforum/',altForum, name='altForum'),
    path('yorum/',yorum, name='yorum'),
    path('olustur/',create, name='olustur'),
]
