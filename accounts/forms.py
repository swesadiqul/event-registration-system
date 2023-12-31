from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


#create forms here
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
