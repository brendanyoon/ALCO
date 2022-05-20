from django import forms
from django.forms import TextInput, IntegerField
from .models import *
from django.forms import inlineformset_factory

class Quest_Creation_Form(forms.ModelForm):
    class Meta:
        model = Quest
        fields =('title','total_exp', 'is_required')

class Obstacle_Creation_Form(forms.ModelForm):
    class Meta:
        model = Obstacle
        fields = ('quest_id', 'obstacle_id', 'description', 'num_images', 'obstacle_type')

class Multiple_Choice_Creation_Form(forms.ModelForm):
    class Meta:
        model = Multiple_Choice
        fields = ('obstacle_id', 'num_choices', 'answer')

class Answer_Choice_Creation_Form(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('obstacle_id', 'choice_id', 'choice_desc', 'exp')