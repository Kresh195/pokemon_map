from django.db import models  # noqa F401


class Pokemon(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.Name)


class PokemonEntity(models.Model):
    Pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    Lat = models.FloatField()
    Lon = models.FloatField()

# your models here
