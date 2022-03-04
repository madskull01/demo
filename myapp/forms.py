from django.forms import ModelForm
from .models import Emp,Register,Login

class EmpForm(ModelForm):
    class Meta:
        model=Emp
        fields='__all__'

class RegisterForm(ModelForm):
    class Meta:
        model=Register
        fields='__all__'

class LoginForm(ModelForm):
    class Meta:
        model=Login
        fields='__all__'