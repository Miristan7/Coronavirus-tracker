from django.db import models

class Articles(models.Model):
    question = models.CharField(max_length=120)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"



