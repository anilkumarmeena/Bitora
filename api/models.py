from django.db import models


class Questions(models.Model):
    # Questions titile
    title = models.CharField(max_length=255, null=False)
    # detail explain of question
    content = models.TextField()
    # posting time 
    time = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.title