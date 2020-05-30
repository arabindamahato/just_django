from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    ''' this content is used for form in post section it gives 
    charfield with bootstrap class form-control and placeholder,
    id, rows. means whole design instead of textarea in html. 
    *No need to use textarea in html page   '''
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', ) 