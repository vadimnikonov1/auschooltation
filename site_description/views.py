from django.shortcuts import render, redirect
from .forms import ContactForm
from site_description.helper_functions.process_contact_form import process_form_tg


# Create your views here.
def home(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            process_form_tg(contact_form)
            return redirect('contact_form_success')
    else:
        contact_form = ContactForm()
    return render(request, 'site_description/home_landing.html', {'contact_form': contact_form})


def contact(request):
    return render(request, 'site_description/contact_form_success.html')
