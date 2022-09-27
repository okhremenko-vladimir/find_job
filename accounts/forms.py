from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, label='Имя')
    last_name = forms.CharField(max_length=32, label='Фамилия')
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Зарегистрироваться', css_class='btn btn-primary btn-lg btn-block'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'float-left pl-3'
        self.helper.field_class = 'col-lg-12'
        self.helper.layout = Layout(Fieldset('Создайте аккаунт', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2'))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
