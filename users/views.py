from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .forms import UserLogInForm
from users.models import UserProfileStat
from users.helper_functions.user_profile_functions import correct_answers_number


# Create your views here.
def register_or_log_in(request):
    """View for handling one of two post requests on the page of registration/log in"""
    error_dict = {}
    # registration form
    if request.method == 'POST' and request.POST.get('submit') == 'reg':
        user_reg_form = UserRegisterForm(request.POST)
        if user_reg_form.is_valid():
            user_reg_form.save()  # save user to database
            username = user_reg_form.cleaned_data.get('username')
            messages.success(request, f"Аккаунт создан для {username}!")
            return redirect('registration_and_login')
        else:
            error_dict['errors_reg'] = user_reg_form.errors
    else:
        user_reg_form = UserRegisterForm()

    # log in form
    if request.method == 'POST' and request.POST.get('submit') == 'log_in':
        user_log_in_form = UserLogInForm(data=request.POST)
        if user_log_in_form.is_valid():
            username = user_log_in_form.cleaned_data.get('username')  # request.POST['username']
            password = user_log_in_form.cleaned_data.get('password')  # request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('tests')  # redirect to app page
        else:
            error_dict['log_in_errors'] = user_log_in_form.errors
    else:
        user_log_in_form = UserLogInForm()

    return render(request, 'users/login_signup.html', {'user_reg_form': user_reg_form, 'error_dict': error_dict,
                                                       'user_log_in_form': user_log_in_form})


@login_required
def user_profile(request):
    current_user = request.user
    profile_data = UserProfileStat.objects.filter(user_answer__user=current_user)
    if profile_data:
        # if there is data in profile_stats
        answers_len, correct_answers_len = correct_answers_number(profile_data_query=profile_data)
        success_percentage = round(100 * correct_answers_len / answers_len)
    else:
        success_percentage = 0
    context = {'success_percentage': success_percentage}
    return render(request, 'users/profile.html', context)
