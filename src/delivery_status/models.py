from django.db import models

class Delivery_status(models.Model):
    name = models.CharField(max_length=200)
    info = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "yetkazib beruvchini holati"
        verbose_name_plural = "yetkazib beruvchilarni holati"
