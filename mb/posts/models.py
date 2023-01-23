from django.db import models

class Post(models.Model):
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.text[:50] #Отображает до 50 символов поля Text в таблице админ панели
    
    