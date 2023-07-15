from django.db import models
from django.contrib.auth.models import User
from hackathon.models import Hackathon


class DataSubmission(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, null=False, blank=False)
    summ = models.CharField(max_length=500, null=False, blank=True)
    file = models.FileField(upload_to='static/')
    link = models.URLField()
    image = models.ImageField(upload_to='static/')
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    hack = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    def __str__(self):
        return f"Submission #{self.id}"
