from django.db import models
from datetime import date

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(default=date.today(), blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
