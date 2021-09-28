import requests
from auschooltation.configuration.project_configuration import API_LINK, id_dict


def process_form_tg(contact_form):
    text = parse_form_text(contact_form)
    #%2B - '+' encoding
    for chat_id in id_dict.values():
        requests.post(API_LINK + f"/sendMessage?chat_id={chat_id}&text={text}")


def parse_form_text(contact_form):
    user = contact_form.cleaned_data.get('username')
    email = contact_form.cleaned_data.get('email')
    text = contact_form.cleaned_data.get('message_text')
    message_text = f"Сообщение\nUser: {user}\nEmail: {email}\nТекст: {text}"
    return message_text
