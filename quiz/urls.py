from django.urls import path
from .views import *

urlpatterns = [
    path('heart_tones/q1', heart_tones_question_1, name='heart_tones_q1'),
    path('heart_tones/q2', heart_tones_question_2, name='heart_tones_q2'),
    path('heart_tones/q3', heart_tones_question_3, name='heart_tones_q3'),
    path('heart_tones/q4', heart_tones_question_4, name='heart_tones_q4'),
    path('heart_tones/q5', heart_tones_question_5, name='heart_tones_q5'),
    path('heart_tones/q6', heart_tones_question_6, name='heart_tones_q6'),
    path('heart_tones/q7', heart_tones_question_7, name='heart_tones_q7'),
    path('heart_tones/q8', heart_tones_question_8, name='heart_tones_q8'),
    path('heart_tones/q9', heart_tones_question_9, name='heart_tones_q9'),
    path('heart_tones/q10', heart_tones_question_10, name='heart_tones_q10'),
    path('tests/', tests_page, name='tests'),

]
