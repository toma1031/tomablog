from django import forms

class PostForm(forms.Form):
  title = forms.CharField(max_length=30, label= 'Title')
  content =  forms.CharField(label='Contents', widget= forms.Textarea())