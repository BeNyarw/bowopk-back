from django.db import models

# Create your models here.
from django.db import models


class Pokdx(models.Model):
    attack = models.IntegerField()
    classfication = models.CharField(max_length=51)
    defense = models.IntegerField()
    height_m = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    hp = models.IntegerField()
    japanese_name = models.CharField(max_length=33)
    name = models.CharField(max_length=12)
    pokedex_number = models.IntegerField(primary_key=True)
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    type1 = models.CharField(max_length=8)
    type2 = models.CharField(max_length=8, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    generation = models.IntegerField()
    is_legendary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokdx'