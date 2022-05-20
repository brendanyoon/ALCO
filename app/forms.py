from django import forms
from django.forms import TextInput, IntegerField
from .models import Quiz, Quest, Obstacle, Multiple_Choice


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('quizName', 'pdf')

class Quest_Creation_Form(forms.ModelForm):
    class Meta:
        model = Quest
        fields =('title', 'num_questions', 'total_exp', 'is_required')

class Question_Form_Student(forms.ModelForm):
    class Meta:
        model = Multiple_Choice
        fields =('num_choices', 'answer')