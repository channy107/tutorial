from django.db import models


class Curriculum(models.Model):
    name = models.CharField(max_length=255)

class Person(models.Model):
    # Ctrl + P -? parameter 사용법
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name + '/' + str(self.age)