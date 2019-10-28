from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name = "date published")
    def __str__(self):
        return f"Question:{self.id} | {self.question_text}"
    @property
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #wywołaj to wyżej z shella - sprawdz argumenty i dodaj do admin.py zeby sprawdzac w django czy wyswietla kolumne
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f"Question:{self.id} | {self.choice_text}"