from django.contrib.auth import forms as auth_forms
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import User


class LoginForm(auth_forms.AuthenticationForm):
    username = forms.EmailField(
        min_length=6,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class SignupForm(forms.ModelForm):
    email = forms.EmailField(
        min_length=6,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('email',)

    def save(self, request=None, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        # 设置密码
        user.set_password(password)
        if commit:
            user.save()
        return user