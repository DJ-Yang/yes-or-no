from django import forms
from .models import User


age_range = (
    ('10','10대'),
    ('20','20대'),
    ('30','30대'),
    ('40','40대'),
    ('50','50대'),
    ('60','60대')
    )

gender = (
    ('male','남성'),
    ('female','여성')
)

class AddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['gender','age_range']

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['age_range'] = forms.ChoiceField(choices=age_range)
        self.fields['gender'] = forms.ChoiceField(choices=gender)