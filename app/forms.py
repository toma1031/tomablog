from django import forms
from .models import Category

class PostForm(forms.Form):
  category_data =  Category.objects.all()
  category_choise = {}
  for category in category_data:
    category_choise[category] = category
    
  title = forms.CharField(max_length=30, label= 'Title')
  category = forms.ChoiceField(label='Category', widget=forms.Select, choices=list(category_choise.items()))
  content =  forms.CharField(label='Contents', widget= forms.Textarea())
  image = forms.ImageField(label='image', required=False)