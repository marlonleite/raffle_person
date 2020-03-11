from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Person(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Raffle(models.Model):
    number = models.CharField(max_length=10, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number} - {self.person}"


@receiver(pre_save, sender=Raffle)
def fill_number(sender, instance, **kwargs):
    try:
        item = Raffle.objects.latest('number')
        number = item.number
    except Raffle.DoesNotExist:
        number = "0"

    instance.number = str(int(number) + 1).zfill(10)
