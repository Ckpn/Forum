from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name = 'index'),
    path('forum/',forum, name='forum'),
    path('altforum/',altForum, name='altForum'),
    path('comment/',yorum, name='comment'),
    path('olustur/',create, name='olustur'),
]
