from django.db import models




class EventRegistration(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    password = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.full_name} - {self.age}"
    