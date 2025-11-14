from django.db import models

class Design(models.Model):
    image = models.ImageField(upload_to="designs/", blank=True, null=True)
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    dimensions = models.CharField(max_length=100)
    stitch_details = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} - {self.price}"
