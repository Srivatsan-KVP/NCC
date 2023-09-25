from django.db import models
import uuid

# Create your models here.
class Batch(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    label = models.CharField(max_length=10)

    def __str__(self):
        return self.label
    

class Cadet(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=64)
    batch = models.ForeignKey(to=Batch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name + ' (' + self.batch + ')'
    

