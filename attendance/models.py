from django.db import models
from server.models import Cadet

# Create your models here.
class Entry(models.Model):
    cadet = models.ForeignKey(to=Cadet, on_delete=models.CASCADE)
    date = models.DateField()