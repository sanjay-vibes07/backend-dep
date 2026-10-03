from django.db import models
from django.db import models
class Staff(models.Model):
    name = models.CharField(default='')
    email = models.CharField(unique=True)
    role = models.CharField()
    salary = models.IntegerField()
    attendance = models.IntegerField()

    def __str__(self):
        return self.name 
 
