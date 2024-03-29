from django.db import models

class WaterLevel(models.Model):
    level = models.IntegerField()

    def __str__(self):
        return f"Water Level: {self.level}"
