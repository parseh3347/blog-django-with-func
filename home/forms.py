from django import forms
from .models import Todo

class PostCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    # created =forms.DateTimeField()
    # update =forms.DateTimeField()
    publish =forms.DateTimeField()

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ('title','body','publish')
 