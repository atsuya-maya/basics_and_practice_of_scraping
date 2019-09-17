from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='URL')

class URLandStringForm(URLForm):
    string = forms.CharField(label="Query Parameter", min_length=1)
