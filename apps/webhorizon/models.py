from django.db import models

# Create your models here.
class Jailbreak(models.Model):
    pk_Version = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    Version = models.CharField(max_length=50, blank=False, null=False)
    Desarollador = models.CharField(max_length=100, blank=False, null=True)
    descripcion = models.TextField(blank=False, null=True)

