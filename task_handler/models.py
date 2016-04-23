from django.db import models
from datetime import timedelta
from datetime import datetime
from django.contrib.auth.models import User

class RecurringTask(models.Model):
    user            =       models.ForeignKey(User)
    task_name       =       models.CharField(max_length=120)
    task_type        =       models.CharField(max_length=120, default="recurring")
    description     =       models.TextField(default="")
    frequency       =       models.DurationField(default=timedelta(days=1))
    active          =       models.BooleanField(default=True)

    latest_event    =       models.ForeignKey("RecurringEvent", blank=True, null=True, default = None)

    def __str__(self):
        return self.task_name



class DeadlineTask(models.Model):
    user            =       models.ForeignKey(User)
    task_name       =       models.CharField(max_length=120)
    task_type       =       models.CharField(max_length=120, default="deadline")
    description     =       models.TextField(default = "")
    soft_deadline   =       models.DateTimeField()
    hard_deadline   =       models.DateTimeField()
    active          =       models.BooleanField(default=True)

    def __str__(self):
        return self.task_name 


class RecurringEvent(models.Model):
    task            =       models.ForeignKey(RecurringTask)
    task_name       =       models.CharField(max_length=120)
    completed_time  =       models.DateTimeField()
    started_time    =       models.DateTimeField()

    def __str__(self):
        return self.task_name

class RecurringComment(models.Model):
    event           =       models.ForeignKey(RecurringEvent)
    task_name       =       models.CharField(max_length=120)
    comment         =       models.TextField()
    timestamp       =       models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name

class DeadlineComment(models.Model):
    task            =       models.ForeignKey(DeadlineTask)
    task_name       =       models.CharField(max_length=120)
    comment         =       models.TextField()
    timestamp       =       models.DateTimeField(auto_now=True)

class Notes(models.Model):
    user            =       models.ForeignKey(User)
    task_type       =       models.CharField(max_length=120, default="note")
    # The task type is necessary because this is what is used as a condition
    # in the views.
    title           =       models.CharField(max_length=120)
    text            =       models.TextField()







# Create your models here.
