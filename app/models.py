from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "Region"

class Fruits(models.Model):
    name = models.CharField(max_length=25)
    # o segundo argumento é para evitar a remoção manual
    origin = models.ForeignKey(to=Region, on_delete=models.CASCADE)

    class Meta:
        db_table = "Fruits"
