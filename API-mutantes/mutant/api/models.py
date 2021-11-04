from django.db import models

# Create your models here.

class Mutant(models.Model):
    dna = models.CharField(max_length=500)

    class meta:
        db_table = 'mutant'

    def __str__(self):
        return self.dna