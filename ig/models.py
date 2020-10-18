from django.db import models

# Models
class Post(models.Model):
    post_image = models.ImageField(upload_to = 'posts/')
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=60)
    pub_date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

    def save_post(self):
        self.save()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'posts/')
    bio = models.TextField(max_length=255)

    def save_profile(self):
        self.save()