from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    message_text = forms.CharField(widget=forms.Textarea)

    # placeholders for fields
    username.widget.attrs.update({'placeholder': 'Введите ваше имя'})
    email.widget.attrs.update({'placeholder': 'Введите ваш email'})
    message_text.widget.attrs.update({'placeholder': 'Ваше сообщение'})
