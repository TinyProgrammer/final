from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from utilities.customized_id import create_id
from utilities.utime import UTime
from django.contrib.auth.models import AbstractUser, BaseUserManager
import bcrypt

SALT = b'$2b$12$DcKqcgCo0HvYpEsB/Ax.XO'


class Status(models.Model):
    id = models.AutoField(max_length=36, primary_key=True,  editable=False)
    text = models.CharField(max_length=255)
    value = models.PositiveIntegerField()


class PersonManager(BaseUserManager):
    def create(self, username, password, first_name, last_name, **kwargs):
        person = self.model(username=username, first_name=first_name, last_name=last_name, **kwargs)
        person.set_password(password)
        person.save()
        return person

    def create_superuser(self, username, password, first_name, last_name, **kwargs):
        return self.create(username, password, first_name, last_name,
                           is_admin=True, is_staff=True, is_superuser=True, **kwargs)

    # def filter(self, **kwargs):
    #     password = kwargs.get('password')
    #     if password is not None and type(password) == str:
    #         kwargs['password'] = bcrypt.hashpw(password.encode('utf8'), SALT)
    #     return super(PersonManager, self).get_queryset().filter(**kwargs)
    #
    # def get(self, **kwargs):
    #     password = kwargs.get('password')
    #     if password is not None and type(password) == str:
    #         kwargs['password'] = bcrypt.hashpw(password.encode('utf8'), SALT)
    #     return super(PersonManager, self).get_queryset().get(**kwargs)


class Person(AbstractBaseUser):
    id = models.CharField(max_length=36, primary_key=True, default=create_id)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=60, unique=True, null=False)
    password = models.CharField(max_length=60, null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = PersonManager()

    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']
    USERNAME_FIELD = 'username'

    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode('utf8'), SALT)

    class Meta:
        ordering = ['last_name']


class Field(models.Model):
    id = models.CharField(max_length=36, primary_key=True,
                          editable=False)

    value = models.CharField(max_length=255)


class Collegian(Person):
    study_field = models.ForeignKey(Field, on_delete=models.CASCADE)

    @property
    def study_field_value(self):
        return self.study_field.value


class Professor(Person):
    specialized_fields = models.ManyToManyField(Field)

    @property
    def specialized_fields_value(self):
        field_names = []
        for field in self.specialized_fields.values():
            field_names.append(field.get('value'))

        return field_names


class DepartmentHead(Person):
    specialized_fields = models.ManyToManyField(Field)


class Report(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=create_id)
    collegian = models.ForeignKey(Collegian, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    created = models.PositiveIntegerField(default=UTime.now)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.TextField()

    @property
    def collegian_name(self):
        name = self.collegian.first_name + ' ' + self.collegian.last_name
        return name

    @property
    def professor_name(self):
        name = self.professor.first_name + ' ' + self.professor.last_name
        return name


class WeeklyReport(Report):
    pass


class Request(Report):
    accepted = models.BooleanField()


class FinalProject(Report):
    accepted = models.BooleanField()
    file_path = models.TextField()


class Proposal(Report):
    accepted = models.BooleanField()
