from django.db import models
from user.models import Adress
from payment.models import Payment
from delivery.models import Delivery, Status
from staff.models import Staff

# Create your models here.

class Orders(models.Model):
    address = models.ForeignKey(Adress, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    delivery_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"


