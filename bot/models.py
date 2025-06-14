from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

    
class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    

# models.py
from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"@{self.username}" if self.username else f"User {self.telegram_id}"

    class Meta:
        verbose_name = "Telegram User"
        verbose_name_plural = "Telegram Users"



