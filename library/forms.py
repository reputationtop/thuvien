from dataclasses import field, fields
from tkinter import Label, Widget
from django import forms
from .models import Category , Book, Email,Listing, Comment

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
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        Labels = {
            'comment': ''
        }
        widgets = {"comment": forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'maxlength': '1000'})}