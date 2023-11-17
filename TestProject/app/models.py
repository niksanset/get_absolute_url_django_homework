from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.age}"

    def get_absolute_url(self):
        return f"/users/{self.first_name}"
