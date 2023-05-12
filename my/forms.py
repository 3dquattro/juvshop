from django.contrib.auth.forms import UserCreationForm
from django import forms
from core.models import User
from my.models import Profile, Address
from django.contrib.auth.forms import PasswordChangeForm


class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["email", "name"]


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", max_length=70, required=True)
    last_name = forms.CharField(label="Фамилия", max_length=70, required=True)
    second_name = forms.CharField(label="Отчество", max_length=70, required=False)
    birthdate = forms.DateField(label="Дата рождения", required=True)
    active_address = forms.ModelChoiceField(
        queryset=Address.objects.all(), label="Адрес по умолчанию", required=False
    )

    class Meta:
        model = Profile
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if instance:
            self.fields["active_address"].queryset = instance.address_set.all()


class AddressForm(forms.ModelForm):
    address = forms.CharField(label="Адрес", max_length=200, required=False)

    class Meta:
        model = Address
        exclude = ["profile"]

    def save(self, commit=True):
        address = super().save(commit=False)
        if not address.profile_id:
            address.profile = Profile.objects.get(user=self.request.user)
        if commit:
            address.save()
        return address

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if instance:
            self.fields["address"].initial = instance.address


class ChangePasswordForm(PasswordChangeForm):
    pass
