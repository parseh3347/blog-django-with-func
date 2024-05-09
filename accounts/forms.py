from django import forms


class UserCreateForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    # is_staf=forms.is_staf

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

