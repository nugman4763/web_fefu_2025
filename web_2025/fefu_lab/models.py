from django.db import models
from django.core.exceptions import ValidationError
import re

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True, verbose_name='Логин')
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def clean(self):
        # Валидация логина
        if len(self.username) < 3:
            raise ValidationError({'username': 'Логин должен содержать минимум 3 символа'})
        
        # Валидация пароля
        if len(self.password) < 8:
            raise ValidationError({'password': 'Пароль должен содержать минимум 8 символов'})
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'