from django.db import models
from utilities.customized_id import create_id
from utilities.utime import UTime


class Status(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=create_id, editable=False)
    text = models.CharField(max_length=255)
    value = models.PositiveIntegerField()


class Person(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=create_id)
    primary_key = models.CharField
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['last_name']


class Field(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=create_id,
                          editable=False)

    value = models.CharField(max_length=255)


class Collegian(Person):
    study_field = models.ForeignKey(Field, on_delete=models.CASCADE)

    @property
    def by_field_name(self):
        return self.study_field.value


class Professor(Person):
    specialized_fields = models.ManyToManyField(Field)

    def specialized_fields_value(self):
        field_names = []
        for field in self.specialized_fields.values():
            field_names.append(field.get('value'))

        return field_names


class DepartmentHead(Person):
    specialized_fields = models.ManyToManyField(Field)


class Report(models.Model):
    collegian = models.ForeignKey(Collegian, on_delete=models.CASCADE)
    Professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    created = models.PositiveIntegerField(default=UTime.now)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.TextField()


class WeeklyReport(Report):
    pass


class Request(Report):
    accepted = models.BooleanField()


class FinalProject(Report):
    accepted = models.BooleanField()
    file_path = models.TextField()
