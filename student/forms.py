from django import forms
from .models import UsersAccount
from submission.models import StudentEssay


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'email',

            }
        )
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'password',

            }
        )
    )


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UsersAccount
        fields = ('username', 'password', 'email', 'mobile')

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'email',

            }
        )
    )

    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'username',

            }
        )
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'password',

            }
        )
    )

    mobile = forms.IntegerField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'mobile',

            }
        )
    )


class AddEssayform(forms.ModelForm):
    class Meta:
        model = StudentEssay
        fields = ('title', 'body')

    title = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:5px',
                'placeholder': 'title',

            }
        )
    )

    body = forms.Textarea( )

