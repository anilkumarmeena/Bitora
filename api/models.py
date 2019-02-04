from django.db import models

# Create your models here.\

class Questions(models.Model):
    title= models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField("time of publish")

    def _str_(self):
        return self.title


