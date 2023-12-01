from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Game(models.Model):
    wrongGuesses = models.IntegerField(default=0)
    word = models.CharField(max_length=40)
    wordBlanks = models.CharField(max_length=80)
    origWord = models.CharField(max_length=40)
    prevGuesses = models.CharField(max_length=26)
