from django import forms

class SearchForm(forms.Form):
    result = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite algo que deseja procurar...', 'type': 'search', 'class': 'search'}), label='')