from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length=255, default=" ", blank=True, null=True)

    def __str__(self):
        return self.title

class Queston(models.Model):
    title = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255, blank=True, null=True)
    option4 = models.CharField(max_length=255, blank=True, null=True)
    answer = models.IntegerField( default=1, blank=True, null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)])

    def __str__(self):
        return self.title
    
class Scores(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username