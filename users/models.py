from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'users'
        verbose_name = 'user'


class VerificationCodeModel(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4,unique=True)
    status = models.BooleanField(default=False)
    send_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Code'
        verbose_name_plural = 'Codes'
