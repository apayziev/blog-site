from django.db import models
from helpers.models import BaseModel
# Create your models here.


class FAQ(BaseModel):
    title = models.CharField(max_length=256)
    content = models.TextField()

class ContactUs(BaseModel):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"