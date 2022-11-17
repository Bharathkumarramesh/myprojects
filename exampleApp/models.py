from django.db import models
from colorfield.fields import ColorField


class User(models.Model):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.IntegerField(unique=True, db_index=True)
    color = ColorField(default='#FF0000')

    # def __str__(self):
    #     return self.first_name
