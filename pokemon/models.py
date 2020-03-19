from django.db import models


# Create Pokemon model in Database
class Pokemon(models.Model):
    Name = models.CharField(max_length=255, blank=True, null=True)
    Type1 = models.CharField(max_length=100, blank=True, null=True)
    Type2 = models.CharField(max_length=100, blank=True, null=True)
    Total = models.IntegerField(null=True)
    HP = models.IntegerField(null=True)
    Attack = models.IntegerField(null=True)
    Defense = models.IntegerField(null=True)
    SpAtk = models.IntegerField(null=True)
    SpDef = models.IntegerField(null=True)
    Speed = models.IntegerField(null=True)
    Generation = models.IntegerField(null=True)
    Legendary = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.Name

