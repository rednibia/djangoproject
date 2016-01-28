import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    qtxt = models.CharField(max_length=200)
    pd = models.DateTimeField('date published')
    def __str__(self):
        return self.qtxt
    def publishrec(self):
        return self.pd >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ctxt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.ctxt
