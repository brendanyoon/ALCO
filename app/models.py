from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

string_max_length:int = 250
description_max_length: int = 700

class Professor(models.Model):
    professor_email = models.EmailField(max_length=string_max_length, primary_key=True)
    first_name = models.CharField(max_length=string_max_length)
    last_name = models.CharField(max_length=string_max_length)

class Student(models.Model):
    student_email = models.EmailField(max_length=string_max_length, primary_key=True)
    first_name = models.CharField(max_length=string_max_length)
    last_name = models.CharField(max_length=string_max_length)
    grade = models.DecimalField(max_digits=5, decimal_places=3)
    exp_pts = models.IntegerField(default = 0)

    def exp(self):
        return int("" + self.exp_pts)

class Obstacle(models.Model):
    OBSTACLE_TYPES =[
        'Multiple_Choice',
        'Multiple_Answers',
        'Fill_In_The_Blank'
    ]

    obstacle_id = models.CharField(max_length=string_max_length, primary_key=True)
    description = models.TextField()
    num_images = models.IntegerField()
    image_src_array = ArrayField(ArrayField(models.ImageField(upload_to='app/static/images')))
    obstacle_type = OBSTACLE_TYPES


class Multiple_Choice(Obstacle):
    num_choices = models.IntegerField()
    answer = models.CharField(max_length=string_max_length)
    answer_choices_array = ArrayField(ArrayField(models.TextField(null=True, default='')))

class Multiple_Answers(Obstacle):
    num_choices = models.IntegerField()
    num_answers = models.IntegerField()
    answers_array = ArrayField(ArrayField(models.TextField(null=True, default='')))
    answer_choices_array = ArrayField(ArrayField(models.TextField(null=True, default='')))

class Quest(models.Model):
    title = models.CharField(max_length=string_max_length, primary_key=True)
    num_questions = models.IntegerField()
    total_exp = models.IntegerField()
    obstacles_array = models.ManyToManyField(Obstacle)
    is_required = models.BooleanField()

class Completed_Quest(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    date_completed = models.DateField()
    exp_earned = models.IntegerField()


    

