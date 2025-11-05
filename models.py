from django.db import models

class Design(models.Model):
    # Image field for embroidery design image
    image = models.ImageField(upload_to="designs/", blank=True, null=True)

    # Basic info
    product_name = models.CharField(max_length=200)
    description = models.TextField()

    # Dimensions (like width x height in cm/inches)
    dimensions = models.CharField(max_length=100)

    # Stitch details (like stitch type, count, etc.)
    stitch_details = models.CharField(max_length=200)

    # Price
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # For display in admin
    def __str__(self):
        return (f"{self.product_name}-{self.price}")
