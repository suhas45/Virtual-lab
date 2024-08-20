from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class QuizScore(models.Model):
    username = models.CharField(max_length=100)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    percentage = models.FloatField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.score}/{self.total_questions} ({self.percentage}%)"

