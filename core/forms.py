from django import forms
from core.models import GitUser, Group


class LoginForm(forms.Form):
    username = forms.CharField(max_length=300)
    password = forms.CharField(max_length=300, widget=forms.PasswordInput())


class GitUserForm(forms.ModelForm):

    class Meta:
        model = GitUser
        fields = ['email']

    email = forms.EmailField()


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name']

    name = forms.CharField(max_length=40)
