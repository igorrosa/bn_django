from django import forms

from books.models import Author


class AuthorForm(forms.Form):
    pass
    '''first_name = forms.CharField()
    last_name = forms.CharField()
    public_domain = forms.BooleanField()''' #niewygodne

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = () # albo field jak dodajemy