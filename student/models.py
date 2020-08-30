from django.db import models
from datetime import datetime


class ClassST(models.Model):
    TYPE_CHOICES = (
        (0, "Online"),
        (1, "Offline"),
    )
    classname = models.CharField(max_length=100)
    classtype = models.IntegerField(default=1, choices=TYPE_CHOICES)

    def __str__(self):
        return self.classname


class Students(models.Model):
    GENDER_CHOICES = (
        (0, "Male"),
        (1, "Female"),
    )
    STATE_CHOICES = (
        (0, "Schools"),
        (1, "Works"),
    )
    name = models.CharField(max_length=100)
    birthday = models.DateField(datetime.now())
    gender = models.IntegerField(default=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=100)
    state = models.IntegerField(default=1, choices=STATE_CHOICES)

    def __str__(self):
        return self.name
