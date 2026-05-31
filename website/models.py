from django.db import models

# Create your models here.

class Posts(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=254)
    email = models.EmailField()
    message = models.TextField()
    status =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'پست '
        verbose_name_plural = 'پست ها'
        
    def __str__(self):
        return f"{self.name} - {self.email} - {self.created_at}"