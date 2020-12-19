from django.db import models
from django.conf import settings
from geo.models import Districts

class Adress(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    region = models.ForeignKey(Districts, on_delete=models.CASCADE)
    adress = models.TextField()
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.adress
    class Meta:
        verbose_name = "Manzil"
        verbose_name_plural = "Manzillar"