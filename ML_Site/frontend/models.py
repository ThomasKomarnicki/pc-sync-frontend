from django.db import models


class Faq(models.Model):

    question = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)
    order = models.IntegerField(blank=True)
