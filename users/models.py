from django.db import models
from quiz.models import UserAnswer


# Create your models here.
class UserProfileStat(models.Model):
    user_answer = models.ForeignKey(UserAnswer, on_delete=models.CASCADE)
    is_correct_answer = models.BooleanField()

    class Meta:
        verbose_name = "User Profile Answer"
        verbose_name_plural = "User Profile Answers"

    def __str__(self):
        return f"{self.user_answer} - {self.is_correct_answer}"
