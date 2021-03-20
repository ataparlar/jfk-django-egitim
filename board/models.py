from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=120)
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.surname


class BoardMember(Person):
    duty = models.ForeignKey("Year", on_delete=models.CASCADE)
    year = models.ForeignKey("Duty", on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.surname


class Advisor(Person):
    degree = models.CharField(max_length=100, default="Prof. Dr. ")

    def __str__(self):
        return self.name + " " + self.surname


class Year(models.Model):
    year = models.SmallIntegerField(default=2021)

    def __str__(self):
        return str(self.year)


class Duty(models.Model):
    duty = models.CharField(max_length=60)
    
    def __str__(self):
        return self.duty

