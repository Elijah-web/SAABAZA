from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

class Answer(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
