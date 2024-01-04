from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Contact(models.Model):
    
    name= models.CharField(
        max_length= 255,
        verbose_name='имя'
    )
    phone = models.CharField(
        max_length= 255,
        verbose_name='номер телефона'
    )
    email = models.CharField(
        max_length= 255,
        verbose_name='почта'
    )
    sabject = models.CharField(
        max_length= 255,
        verbose_name='услуга'
    )
    message = models.TextField(
        verbose_name="cообщение"
    )
    status = models.CharField(
        max_length=255, 
        default='Новый'
        )
    is_accepted = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta():
        verbose_name ="запрос на связь"
        verbose_name_plural = 'запросы на связи'