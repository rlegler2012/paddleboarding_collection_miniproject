from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Location: " + self.name

    # This is a way to make sure that the data is saved in the order of the names. Alphabetically sorted
    class Meta:
        ordering = ['name']

