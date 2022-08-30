from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset
from .models import Application


class ApplicationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Отправить отклик'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg'
        self.helper.field_class = 'col-lg'
        self.helper.layout = Layout(Fieldset('Отозваться на вакансию', 'written_username', 'written_phone', 'written_cover_letter'))

    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']

