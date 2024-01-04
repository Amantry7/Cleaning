from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=244,
        verbose_name='Название сайта'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='логотип'
    )
    disc = models.TextField(
        verbose_name= "Описание"
    )
    number = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'   
    )
    addres = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    twitter = models.URLField(
        verbose_name="Url Twitter",
        blank= True, null=True
    )
    Facebook = models.URLField(
        verbose_name="Url Facebook",
        blank= True, null=True
    )
    Instagram = models.URLField(
        verbose_name="Url instagram",
        blank= True, null=True
    )
    gmail = models.EmailField(
        verbose_name='Gmail'
    )
    def __str__(self):
        return self.title
    class Meta():
        verbose_name="Основные настройки"
        verbose_name_plural="Основные настройки"
        
        
class Subject(models.Model):
    title = models.CharField(
        max_length=244,
        verbose_name='название'
    )
    image = models.ImageField(
        upload_to='subject/',
        verbose_name='фото'
    )
    image2 = models.ImageField(
        upload_to='subject/',
        verbose_name='фото'
    )
    price = models.CharField(
        max_length=244,
        verbose_name='цена'
    )
    time = models.CharField(
        max_length=255,
        verbose_name='время' 
    )
    disk= models.TextField(
        verbose_name='описание'   
    )
    def __str__(self):
        return self.title
    class Meta():
        verbose_name= "Услага"
        verbose_name_plural='Услуги'
        
class Client(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    image = models.ImageField(
        upload_to='client_logo',
        verbose_name='фото'
    )
    disc = models.TextField(
        verbose_name='Отзыв'
    )
    def __str__(self):
        return self.name
    class Meta():
        verbose_name='Отзыв'
        verbose_name_plural='Отзавы'
class Partners(models.Model):
    image = models.ImageField(
        upload_to='partners/',
        verbose_name='фото'
    )
    class Meta():
        verbose_name="Партнер"
        verbose_name_plural="Партнеры"