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
    exp_pts = models.IntegerField()

class Quest(models.Model):
    title = models.CharField(max_length=string_max_length, primary_key=True)
    total_exp = models.IntegerField()
    is_required = models.BooleanField()

    def get_num_questions(self):
        return self.num_questions

class Obstacle(models.Model):
    class ALL_OBSTACLE_TYPES(models.TextChoices):
        MULTIPLE_CHOICE = 'Multiple_Choice',
        MULTIPLE_ANSWERS = 'Multiple_Answers',
        FILL_IN_BLANK = 'Fill_In_The_Blank'

    quest_id = models.ForeignKey(Quest, null=True, on_delete=models.CASCADE)
    obstacle_id = models.CharField(max_length=string_max_length, primary_key=True)
    description = models.TextField()
    num_images = models.IntegerField()
    obstacle_type = models.CharField(max_length=string_max_length, choices=ALL_OBSTACLE_TYPES.choices, default=ALL_OBSTACLE_TYPES.MULTIPLE_CHOICE)

class Multiple_Choice(models.Model):
    obstacle_id = models.ForeignKey(Obstacle, null=True, on_delete=models.CASCADE)
    num_choices = models.IntegerField()
    answer = models.TextField()

class Multiple_Answers(models.Model):
    obstacle_id = models.ForeignKey(Obstacle, null=True, on_delete=models.CASCADE)
    num_choices = models.IntegerField()
    num_answers = models.IntegerField()
    answers_array = ArrayField(ArrayField(models.IntegerField()))

class Choice(models.Model):
    choice_id = models.CharField(max_length=string_max_length)
    obstacle_id = models.ForeignKey(Obstacle, null=True, on_delete=models.CASCADE)
    choice_desc = models.TextField()
    exp = models.IntegerField()

class Quest_Images(models.Model):
    obstacle_id = models.ForeignKey(Obstacle, null=True, on_delete=models.CASCADE)
    image = models.ImageField()

class Completed_Quest(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    date_completed = models.DateField()
    exp_earned = models.IntegerField()


    

