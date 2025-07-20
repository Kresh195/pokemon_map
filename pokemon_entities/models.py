from django.db import models  # noqa F401


class Pokemon(models.Model):
    Title_en = models.CharField(max_length=200)
    Title_ru = models.CharField(max_length=200, default="Покемон")
    Image = models.ImageField(null=True, blank=True)
    Description = models.CharField(max_length=400, default="Описание покемона")

    def __str__(self):
        return self.Title_en


class PokemonEntity(models.Model):
    Pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    Lat = models.FloatField()
    Lon = models.FloatField()

    Appeared_at = models.DateTimeField()
    Disapeared_at = models.DateTimeField()

    Level = models.IntegerField(default=10)
    Health = models.IntegerField(default=200)
    Strength = models.IntegerField(default=30)
    Defence = models.IntegerField(default=15)
    Stamina = models.IntegerField(default=20)

    def __str__(self):
        return self.Pokemon.Title_en
# your models here
