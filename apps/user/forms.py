from django import forms

from apps.user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=255)
    password = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        check = User.objects.filter(email=email)
        if check:
            raise forms.ValidationError("Пользователь с таким E-mail уже существует")
        return email

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password == password_confirm:
            return password_confirm
        raise forms.ValidationError("Пароли не совпадают")
    class Meta:
        model = User
        fields = ['username', 'image', 'first_name', 'last_name', 'email', 'phone', 'about', 'password', 'password_confirm']
