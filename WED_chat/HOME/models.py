
from django.db import models


class question(models.Model):
    chude = models.CharField(max_length=200)
    cauhoi = models.CharField(max_length=500)
    traloi = models.CharField(max_length=5000)

    def __str__(self) -> str:
        return f"{self.chude} "
    






