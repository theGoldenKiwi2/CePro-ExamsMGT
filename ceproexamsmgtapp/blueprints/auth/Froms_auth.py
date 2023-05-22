from wtforms_alchemy import ModelForm
from ceproexamsmgtapp.models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
