from django.contrib import admin
from .models import Professor, Student, Quest, Obstacle, Multiple_Choice, Multiple_Answers, Completed_Quest

admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Quest)
admin.site.register(Obstacle)
admin.site.register(Multiple_Choice)
admin.site.register(Multiple_Answers)
admin.site.register(Completed_Quest)
# admin.site.register(Quiz)



