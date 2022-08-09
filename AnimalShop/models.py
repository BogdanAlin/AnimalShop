from django.db import models


class AnimalDetail(models.Model):
    NUTRITION_TYPES = [
        ("car", "carnivore"),
        ("omn", "omnivore"),
        ("hrv", "herbivore")
    ]
    name = models.CharField(max_length=32,
                            null=False,
                            blank=False,
                            editable=True)
    weight = models.FloatField(max_length=32,
                               null=False,
                               blank=False,
                               editable=True)
    height = models.FloatField(max_length=32,
                               null=False,
                               blank=False,
                               editable=True)
    color = models.CharField(max_length=32,
                             null=False,
                             blank=False,
                             editable=True)
    behaviour = models.CharField(max_length=128,
                                 null=False,
                                 blank=False,
                                 editable=True)
    nutrition = models.CharField(max_length=3,
                                 null=False,
                                 blank=False,
                                 editable=True,
                                 choices=NUTRITION_TYPES)


class Animal(models.Model):
    ANIMAL_RACES = [
        ("dog", "Dog"),
        ("cat", "Cat"),
        ("prt", "Parrot"),
        ("fsh", "Fish")
    ]
    name = models.CharField(max_length=64,
                            null=False,
                            blank=False,
                            editable=True)
    age = models.IntegerField(null=False,
                              blank=False,
                              editable=True)
    race = models.CharField(max_length=3,
                            choices=ANIMAL_RACES)
    detailsID = models.ForeignKey(AnimalDetail, on_delete=models.CASCADE)
