from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .question_options import heart_tones_questions
from quiz.helper_functions.process_views import process_view


# Create your views here.

@login_required
def heart_tones_question_1(request):
    res = process_view(request=request, question_num=1, heart_tone_choice=heart_tones_questions.HEART_TONE_1_CHOICES,
                       redirect_page='heart_tones_q2', render_page='quiz/heart_tones_q1.html', form_name='q1_form')
    return res


@login_required
def heart_tones_question_2(request):
    res = process_view(request=request, question_num=2, heart_tone_choice=heart_tones_questions.HEART_TONE_2_CHOICES,
                       redirect_page='heart_tones_q3', render_page='quiz/heart_tones_q2.html', form_name='q2_form')
    return res


@login_required
def heart_tones_question_3(request):
    res = process_view(request=request, question_num=3, heart_tone_choice=heart_tones_questions.HEART_TONE_3_CHOICES,
                       redirect_page='heart_tones_q4', render_page='quiz/heart_tones_q3.html', form_name='q3_form')
    return res


@login_required
def heart_tones_question_4(request):
    res = process_view(request=request, question_num=4, heart_tone_choice=heart_tones_questions.HEART_TONE_4_CHOICES,
                       redirect_page='heart_tones_q5', render_page='quiz/heart_tones_q4.html', form_name='q4_form')
    return res


@login_required
def heart_tones_question_5(request):
    res = process_view(request=request, question_num=5, heart_tone_choice=heart_tones_questions.HEART_TONE_5_CHOICES,
                       redirect_page='heart_tones_q6', render_page='quiz/heart_tones_q5.html', form_name='q5_form')
    return res


@login_required
def heart_tones_question_6(request):
    res = process_view(request=request, question_num=6, heart_tone_choice=heart_tones_questions.HEART_TONE_6_CHOICES,
                       redirect_page='heart_tones_q7', render_page='quiz/heart_tones_q6.html', form_name='q6_form')
    return res


@login_required
def heart_tones_question_7(request):
    res = process_view(request=request, question_num=7, heart_tone_choice=heart_tones_questions.HEART_TONE_7_CHOICES,
                       redirect_page='heart_tones_q8', render_page='quiz/heart_tones_q7.html', form_name='q7_form')
    return res


@login_required
def heart_tones_question_8(request):
    res = process_view(request=request, question_num=8, heart_tone_choice=heart_tones_questions.HEART_TONE_8_CHOICES,
                       redirect_page='heart_tones_q9', render_page='quiz/heart_tones_q8.html', form_name='q8_form')
    return res


@login_required
def heart_tones_question_9(request):
    res = process_view(request=request, question_num=9, heart_tone_choice=heart_tones_questions.HEART_TONE_9_CHOICES,
                       redirect_page='heart_tones_q10', render_page='quiz/heart_tones_q9.html', form_name='q9_form')
    return res


@login_required
def heart_tones_question_10(request):
    res = process_view(request=request, question_num=10, heart_tone_choice=heart_tones_questions.HEART_TONE_10_CHOICES,
                       redirect_page='profile', render_page='quiz/heart_tones_q10.html', form_name='q10_form')
    return res


@login_required
def tests_page(request):
    return render(request, 'quiz/tests.html')