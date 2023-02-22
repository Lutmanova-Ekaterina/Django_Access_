from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from catalog.forms_mixins import StyleFormMixin
from users.models import User


class CustomEditUserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar')


class CustomRegisterUserForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
