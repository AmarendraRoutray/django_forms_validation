from django.db import models

# Create your models here.

class School(models.Model):
    Sname = models.CharField(max_length=100)
    Sprincipal = models.CharField(max_length=100)
    Sloc = models.CharField(max_length=100)
    email = models.EmailField(default='abc@mail.com')
    reEnterEmail = models.EmailField(default='abc@mail.com')
    
    def __str__(self):
        return self.Sname