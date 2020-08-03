from django import forms
from .models import User
from .region import Sigunu

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

sido = (
    ('서울','서울'),
    ('인천','인천'),
    ('대전','대전'),
    ('광주','광주'),
    ('대구','대구'),
    ('부산','부산'),
    ('울산','울산'),
    ('경기','경기'),
    ('충북','충북'),
    ('충남','충남'),
    ('전북','전북'),
    ('전남','전남'),
    ('강원','강원'),
    ('경북','경북'),
    ('경남','경남'),
    ('제주','제주'),    
)

class AddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['gender','age_range']

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['age_range'] = forms.ChoiceField(
            label=False,
            choices=age_range,
            )
        self.fields['gender'] = forms.ChoiceField(
            label=False,
            choices=gender,
            )
    

class regionForm(forms.Form):
    class Meta:
        model = User
        fields = ['sido','sigungu']

    def __init__(self, *args, **kwargs):
        super(regionForm, self).__init__(*args, **kwargs)
        
        _sido = '서울'
        print(args)
        for arg in args:
            for k,v in arg.items():
                if k == 'sido':
                    _sido = v

        self.fields['sido'] = forms.ChoiceField(
            label=False,
            choices=sido,
        )
        self.fields['sigungu'] = forms.ChoiceField(
            label=False,
            choices=Sigunu().get_list(_sido)
        )

    def set_region(self, selected_sido='서울'):
        self.fields['sido'] = forms.ChoiceField(
            label=False,
            choices=sido,
            initial=selected_sido,            
        )
        self.fields['sigungu'] = forms.ChoiceField(
            label=False,
            choices=Sigunu().get_list(sigunu=selected_sido),         
        )

        return self