from django.db import models

# Create your models here.
class Create_notes(models.Model):
    note=models.TextField(max_length=700)
    contact=models.CharField(max_length=12)
    created_date=models.DateTimeField(auto_now_add=True)
