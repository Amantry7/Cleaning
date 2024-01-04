from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя",
        blank=True, null=True
    )
    email = models.CharField(
        max_length=255,
        verbose_name="почта",
        blank=True, null=True
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="номер телофена",
        blank=True, null=True
    )
    sabject = models.CharField(
        max_length=100,
        verbose_name="Услуга"
    )
    message = models.DateTimeField(
        auto_now_add=True,
        verbose_name="сообщение"
    )

    def __str__(self):
        return str(self.username)
    
    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграма"