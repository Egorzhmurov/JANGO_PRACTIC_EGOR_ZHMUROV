from django.db import models

# Таблиця для Питань
class Question(models.Model):
    question_text = models.CharField(max_length=200) # Текст питання
    pub_date = models.DateTimeField("date published") # Дата публікації

# Таблиця для Варіантів відповідей
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Прив'язка до питання
    choice_text = models.CharField(max_length=200) # Текст відповіді
    votes = models.IntegerField(default=0) # Кількість голосів (спочатку 0
