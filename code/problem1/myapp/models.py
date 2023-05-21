from django.db import models

# Create your models here.
class Task(models.Model):
    Topic = models.CharField(max_length=100)
    Detail = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):#ref field name obj->str  show data on admin page
        return "Topic="+self.Topic+","+str(self.Detail)