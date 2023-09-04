from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True, blank=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username
