from django.db import models

class Delivery(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    info = models.CharField(max_length=2000)
    status = models.IntegerField(default=1, choices=[(1, 'activate'),(0,'Deactivate')])
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Yetkazib berish"
        verbose_name_plural = "yetkazib berivchilar"
