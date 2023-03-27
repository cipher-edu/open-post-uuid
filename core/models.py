from django.db import models
import uuid
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=150,verbose_name='Kompaniya nomi')
    about = models.TextField(verbose_name='Kompaniya haqida')
    logo = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True) # bazada idlarni takrorlamaslik unique=true

    def __str__(self):
        return self.name