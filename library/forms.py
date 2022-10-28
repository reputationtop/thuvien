from dataclasses import field, fields
from tkinter import Label, Widget
from django import forms
from .models import Category , Book, Email,Listing ,active_all

class NewbookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['namebook', 'image', 'description','numbe_book', 'bid', 'category']
        widgets = {
            'namebook': forms.TextInput( attrs={'class': 'form-control'}),
            'image': forms.FileInput( attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows':2, 'maxlength': 600, 'class': 'form-control'}),
            'numbe_book': forms.NumberInput(attrs={'class': 'form-control', 'min':1}),
            'bid': forms.NumberInput(attrs={'class': 'form-control','min':1000 }),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }
class NewemailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['recipients', 'subject','body']
        Widget = {
            'recipients': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput( attrs={'maxlength': 255,'class': 'form-control'}),
            'body': forms.TextInput(attrs={'rows':2, 'class': 'form-control'}),
        }
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        Labels = {
            'name': ''
        }
        widgets = {"name": forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'maxlength': '300'})}
class CommentsForm(forms.ModelForm):
    class Meta:
        model = active_all
        fields = ['reason']
        Labels = {
            'reason': ''
        }
        widgets = {"reason": forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'maxlength': '1000'})}
    