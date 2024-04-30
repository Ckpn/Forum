from django.forms import ModelForm
from .models import *

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title','content','image']
        
        def __init__(self, *args, **kwargs):
            super(CommentForm, self).__init__(*args,**kwargs)
            #self.fields['name'].widget.attrs.update({'class': 'form-control'})
            for title, field in self.fields.items():
                field.widget.attrs.update({'class':'form-control'})