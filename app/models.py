from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

string_max_length: int = 250
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
    exp_pts = models.IntegerField(default=0)

    def exp(self):
        return int(self.exp_pts)

    def fname(self):
        return str(self.first_name)


class Obstacle(models.Model):
    class ALL_OBSTACLE_TYPES(models.TextChoices):
        MULTIPLE_CHOICE = 'Multiple_Choice',
        MULTIPLE_ANSWERS = 'Multiple_Answers',
        FILL_IN_BLANK = 'Fill_In_The_Blank'

    obstacle_id = models.CharField(max_length=string_max_length, primary_key=True)
    description = models.TextField()
    num_images = models.IntegerField()
    image1 = models.ImageField(upload_to='answers')
    image2 = models.ImageField(upload_to='answers')
    image3 = models.ImageField(upload_to='answers')
    image4 = models.ImageField(upload_to='answers')
    obstacle_type = models.CharField(max_length=string_max_length, choices=ALL_OBSTACLE_TYPES.choices, default=ALL_OBSTACLE_TYPES.MULTIPLE_CHOICE)



class Multiple_Choice(Obstacle):
    num_choices = models.IntegerField()
    answer = models.CharField(max_length=string_max_length)
    # answer_choices_array = ArrayField(ArrayField(models.TextField(null=True, default='{choice}')), default='{choice}')


class Multiple_Answers(Obstacle):
    num_choices = models.IntegerField()
    num_answers = models.IntegerField()
    # answers_array = ArrayField(ArrayField(models.TextField(null=True, default='')), default='{choice}')
    # answer_choices_array = ArrayField(ArrayField(models.TextField(null=True, default='{choice}')), default='{choice}')


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


# Nonfunctioning Quiz model - to be updated for displaying quizzes in prof-quizzes.html
class Quiz(models.Model):
    quizName = models.CharField(max_length=string_max_length)
    pdf = models.FileField(upload_to='quizzes/pdfs/')

    def __str__(self):
        return self.quizName


