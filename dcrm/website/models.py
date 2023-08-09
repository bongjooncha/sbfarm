from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    #수정된프로젝트
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    city = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 20)
    sex = models.CharField(max_length=10)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")