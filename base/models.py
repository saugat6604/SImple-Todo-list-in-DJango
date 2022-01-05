from django.db import models
from django.db.models.fields.related import ForeignKey, create_many_to_many_intermediary_model
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering =['complete']

