from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(blank=True, null=True)
    age = models.DecimalField(decimal_places=0, max_digits=2)
    goal = models.TextField(blank=False,null=False)
    placement = models.BooleanField(default=False) #null=True, default=False
