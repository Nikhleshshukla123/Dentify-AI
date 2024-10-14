from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email','phone','first_name','gender')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('phone','first_name', 'last_name', 'gender')
        readonly_fields = ('email',)


