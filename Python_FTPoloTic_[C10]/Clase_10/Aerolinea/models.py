from django.db import models
from django.db.models import Model as MD
from django.db.models.deletion import CASCADE

# Create your models here.
class Aeropuerto(MD):
    codigo = models.CharField(max_length=3)
    ciudad = models.CharField(max_length=64)

    def __str__(self):
        return (f"{self.ciudad} ({self.codigo})")


class Aerolinea(MD):
    origen = models.ForeignKey(Aeropuerto, on_delete=CASCADE, related_name="salidas")
    destino = models.ForeignKey(Aeropuerto, on_delete=CASCADE, related_name="arribos")
    duracion = models.IntegerField()

    def __str__(self):
        return (f"{self.id}: {self.origen} a {self.destino}")