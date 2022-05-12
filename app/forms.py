from django import forms
from django.forms import TextInput, IntegerField
from .models import Quest, Obstacle, Multiple_Choice, Multiple_Answers

class Quest_Creation_Form(forms.ModelForm):
    class Meta:
        model = Quest
        fields =('title', 'num_questions', 'total_exp', 'is_required')

#class Obstacle_Creation_Form(forms.ModelForm):
#    class Meta:

