from django.db import models

# Create your models here.

class FoodCategory(models.Model):
    name = models.CharField(max_length = 100)
    icon = models.ImageField(upload_to='images/')

class Team(models.Model):
    name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='images/')

class Reservalition(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 13)
    reservedDate = models.DateField()
    reservatiuonTime = models.TimeField()
    comments = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Murojaatlar ro'yxati"
        verbose_name_plural = "Murojaatlar"
        ordering = ("id",)
    