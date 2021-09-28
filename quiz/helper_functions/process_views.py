from django.shortcuts import render, redirect
from quiz.forms import QuestionForm
from quiz.models import UserAnswer, Question
from users.models import UserProfileStat


def process_view(request, question_num: int, heart_tone_choice: list, redirect_page: str, render_page: str,
                 form_name: str):
    """Function for processing question views in order to shorten repeated code"""
    question = Question.objects.get(id=question_num)
    if request.method == 'POST':
        q_form = QuestionForm(heart_tone_choice, request.POST)
        if q_form.is_valid():
            current_user = request.user
            answer = q_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            add_to_user_profile(user_answer_rec=ua)  # save to user_profile
            return redirect(redirect_page)
    else:
        q_form = QuestionForm(heart_tone_choice)
    return render(request, render_page, {form_name: q_form, 'question': question})


def add_to_user_profile(user_answer_rec):
    """
    Function for checking answers correctness and saving them in UserProfileStat model
    :param user_answer_rec: user_answer record in database
    :return: None
    """
    if user_answer_rec.user_answer == user_answer_rec.question.get_correct_answer():
        user_profile = UserProfileStat(user_answer=user_answer_rec, is_correct_answer=True)
        user_profile.save()
    else:
        user_profile = UserProfileStat(user_answer=user_answer_rec, is_correct_answer=False)
        user_profile.save()


