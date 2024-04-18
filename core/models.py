from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='', upload_to='Users/Profile')
    bio = models.CharField(max_length=250)
    joine_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
        return self.user.username