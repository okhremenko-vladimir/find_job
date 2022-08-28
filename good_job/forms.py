from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset
from .models import Application


class ApplicationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Записаться на пробный урок'))
        self.helper.form_class = 'card mt-4 mb-3'
        self.helper.label_class = 'mb-1 mt-2'
        self.helper.field_class = 'col-lg-8'
        #self.helper.layout = Layout(Fieldset('Вас зовут', 'Ваш телефон', 'Сопроводительное письмо'))

    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        # 'vacancy', 'user'
