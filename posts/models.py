from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()



class PostModel(models.Model):
    image = models.ImageField(upload_to='posts')
    title = models.CharField(max_length=128)
    description = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')



    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'posts'
        verbose_name = 'post'





