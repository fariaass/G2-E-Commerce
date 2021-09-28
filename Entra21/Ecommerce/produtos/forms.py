from django import forms

class SearchForm(forms.Form):
    result = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Type Something to Search...", 'required':True, 'type': 'search'}), label='')