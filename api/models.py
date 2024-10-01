from django.db import models

class SerialNumber(models.Model):
    serial_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serial_number
