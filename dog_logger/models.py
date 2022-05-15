from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class ActionType(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class ActionHistory(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    action_date = models.DateTimeField()

