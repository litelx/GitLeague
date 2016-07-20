from django import forms
# from django.utils.encoding import smart_unicode

from core.models import GitUser, Group


class LoginForm(forms.Form):
    username = forms.CharField(max_length=300)
    password = forms.CharField(max_length=300, widget=forms.PasswordInput())


class GitUserForm(forms.ModelForm):

    class Meta:
        model = GitUser
        fields = ['username']

    username = forms.CharField(max_length=40)


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name']

    name = forms.CharField(max_length=40)


# class EditGroupForm(forms.ModelForm):
#
#     class Meta:
#         model = Group
#         fields = ['name']
#
#     name = forms.CharField(max_length=40)
#     # git_users = forms.ModelMultipleChoiceField(queryset=GitUser.objects.all(), widget=forms.CheckboxSelectMultiple())
#
#     def __init__(self, *args, **kwargs):
#         super(EditGroupForm, self).__init__(*args, **kwargs)
#         # self.fields['git_users'].queryset = GitUser.objects.all()



