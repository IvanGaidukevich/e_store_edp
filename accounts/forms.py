from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from accounts.models import Profile, Address


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-input-class'}), label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'text-input-class'}), label="Пароль")


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, min_length=3, required=True, label="Логин")
    first_name = forms.CharField(max_length=30, required=True, label='Имя')
    last_name = forms.CharField(max_length=150, required=True, label='Фамилия')
    email = forms.EmailField(max_length=254, required=True, label='Email')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())
    birth_date = forms.DateField(required=True, label='Дата рождения', widget=forms.TextInput(attrs={'type': 'date'}))
    tel = forms.CharField(max_length=11, required=True, label='Телефон')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

            profile = Profile.objects.get(user=user)
            profile.birth_date = self.cleaned_data.get('birth_date')
            profile.tel = self.cleaned_data.get('tel')
            profile.save()

        return user


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'tel']
        labels = ['Дата рождения', 'телефон']


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput())
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput())
    new_password2 = forms.CharField(label="Новый пароль (подтверждение)", widget=forms.PasswordInput())


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'address', 'postal_code']