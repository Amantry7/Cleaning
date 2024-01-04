from django.db import models

# Create your models here.
class About(models.Model):
    disc = models.TextField(
        verbose_name='описание'
    )
    image = models.ImageField(
        upload_to="about/",
        verbose_name='фото'
    )
    def __str__(self):
        return self.disc
    class Meta():
        verbose_name ="О нас"
        verbose_name_plural="О нас"
    
class Team(models.Model):
    image = models.ImageField(
        upload_to="team/",
        verbose_name='фото'   
    )
    name= models.CharField(
        max_length=355,
        verbose_name='имя'
    )
    disc = models.TextField(
        verbose_name='описание'
    )
    phone= models.CharField(
        max_length=255,
        verbose_name='номер телефона'
    )
    def __str__(self):
        return self.name
    class Meta():
        verbose_name="Команда"
        verbose_name_plural='Команды'