from django import forms

class CreatePostFrom(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=50)
    #description = forms.TextField()
    #timeStamp = forms.DateTimeField('Date published')