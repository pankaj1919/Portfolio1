from django.forms import ModelForm
from .models import *

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude=['user']


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username']
# ['first_name', 'last_name', 'email', 'username']