from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=50)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)


class Role(models.Model):
    title = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)

class Activity(models.Model):
    name = models.CharField(max_length=50)
    over_seer = models.ForeignKey(Role,on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=50)
    units = models.IntegerField()
    number_of_labourers = models.IntegerField()
    volumes_transacted = models.FloatField()

class InspectionPoint(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)


class Question(models.Model):
    inspection_point = models.ForeignKey(InspectionPoint, on_delete=models.CASCADE)
    is_boolean = models.BooleanField(default=False)
    qn_content = models.TextField()


class Status(models.Model):
    STATUS1=(
        ('Y', 'Yes'),
        ('N', 'No')
    )

    STATUS2=(
        ('G', 'Good'),
        ('F', 'Fair'),
        ('B', 'Bad')
    )
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    if question.is_boolean:
        status = models.CharField(max_length=1, choices = STATUS1)
    else:
        status = models.CharField(max_length=1, choices = STATUS2)
