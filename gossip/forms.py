from django import forms
from gossip.models import Link
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LinkForm(forms.ModelForm):
        class Meta:
            model = Link
            exclude = ("submitter", "rank_score")