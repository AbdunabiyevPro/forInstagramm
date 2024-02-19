from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()



class PostModel(models.Model):
    image = models.ImageField(upload_to='posts')
    title = models.CharField(max_length=128)
    description = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'posts'
        verbose_name = 'post'


class CommentModel(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='comment')
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name='comment')
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment



    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = 'Comment'


