from django.db import models
from utilities.customized_id import create_id


class Person(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=create_id)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['last_name']


class Field(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=create_id, editable=False)
    value = models.CharField(max_length=255)


class Role(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=create_id, editable=False)
    value = models.CharField(max_length=255)


class Collegian(Person):
    study_field = models.ForeignKey(Field, on_delete=models.CASCADE)


class Professor(Person):
    specialized_fields = models.ManyToManyField(Field)
    rolls = models.ManyToManyField(Role)
