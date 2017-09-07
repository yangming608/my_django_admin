from django.db import models


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    email = models.EmailField()
    age = models.IntegerField()
    def __str__(self):
        return f'{self.user}-{self.email}-{self.age}'


