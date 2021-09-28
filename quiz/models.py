from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    section = models.ForeignKey('Section', default='Section', on_delete=models.SET_DEFAULT)
    question_text = models.TextField()
    question_audio = models.FileField(upload_to='question_audio')

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def get_correct_answer(self):
        return self.answer.answer_text

    def __str__(self):
        return f"{self.question_text}"


class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return f"{self.answer_text}"


class Section(models.Model):
    section_name = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"

    def __str__(self):
        return f"{self.section_name}"


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=60)

    class Meta:
        verbose_name = "User answer"
        verbose_name_plural = "User answers"

    def __str__(self):
        return f"{self.user.username} {self.user_answer}"
