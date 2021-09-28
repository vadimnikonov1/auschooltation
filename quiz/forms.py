from django import forms


class QuestionForm(forms.Form):

    def __init__(self, options_list, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['options'] = forms.CharField(label='', widget=forms.RadioSelect(choices=options_list))
