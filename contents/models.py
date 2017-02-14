from django.db import models


class University(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    rank = models.IntegerField()
    image = models.ImageField(upload_to='images/university/')

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    description = models.CharField(max_length=5000)
    degree = (('M', 'Master'),
              ('P', 'PHD'))
    minimum_toefl = models.IntegerField()
    minimum_gre = models.IntegerField()
    other_prerequisite = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
