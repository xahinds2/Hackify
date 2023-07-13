from django.db import models


class Hackathon(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    sub_typ = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    reward = models.DecimalField(max_digits=8, decimal_places=2)
    prize = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title
