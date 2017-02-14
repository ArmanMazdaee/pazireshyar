from django.forms import EmailField, CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class SignupForm(UserCreationForm):
    email = EmailField(
        label=_('Email address'),
        required=True,
    )
    first_name = CharField(
        label=_('first name'),
        required=True,
    )
    last_name = CharField(
        label=_('last name'),
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
