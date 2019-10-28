from django.contrib import admin
from .models import Question, Choice

# Register your models here.

#1sza mozliwosc zrobienia tego
class QuestionAdmin(admin.ModelAdmin):
    #wyświetlanie bazy danych w CMS
    list_display = ['id', 'question_text', 'pub_date']
admin.site.register(Question, QuestionAdmin)

#2ga mozliwosc zrobienia tego
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
