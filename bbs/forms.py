#coding:utf-8
from django import forms
from django.core.exceptions import ValidationError
import re

class RegistForm(forms.Form):
    """
    Regist Form
    """

    def name_validate(value):
        name_re = re.compile(r'^[a-zA-Z]{1}\w+$')
        if not name_re.match(value):
            raise ValidationError('用户名格式错误')

    email = forms.EmailField(
            label = '邮箱',
            widget=forms.EmailInput(attrs = {
                'class': 'form-control',
                'placeholder': '输入邮箱',
                'required': 'True'
            })
    )

    username = forms.CharField(
            label = '用户名',
            max_length = 20,
            validators=[name_validate],
            widget = forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': '输入用户名',
                'required': 'True'
            })
    )

    password1 = forms.CharField(
            label = '密码',
            min_length = 8,
            max_length = 20, required = True,
            widget = forms.PasswordInput(attrs = {
                'class': 'form-control',
                'placeholder': '输入密码',
                'required': 'True'
            })
    )

    password2 = forms.CharField(
            label = '密码',
            min_length = 8,
            max_length = 20, required = True,
            widget = forms.PasswordInput(attrs = {
                'class': 'form-control',
                'placeholder': '再次输入密码',
                'required': 'True'
            })
    )

class LoginForm(forms.Form):
    email = forms.EmailField(
            widget=forms.EmailInput(attrs = {
                'class': 'form-control',
                'placeholder': '输入邮箱',
                'required': 'True'
                })
    )

    password = forms.CharField(
            widget = forms.PasswordInput(attrs = {
                'class': 'form-control',
                'placeholder': '输入密码',
                'required':'True'
            })
    )
