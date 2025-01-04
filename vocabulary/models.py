from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    korean_word = models.CharField(max_length=100)
    english_translation = models.CharField(max_length=200)
    example_sentence = models.TextField(blank=True)

    def __str__(self):
        return self.korean_word
