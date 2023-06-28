from django.db import models
from users.models import CustomUser


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateField()

    def __str__(self):
        return str(self.user) + ": " + str(self.text)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateField()

    def __str__(self):
        return str(self.user) + ' at "' + str(self.post) + '": ' + str(self.text)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_added = models.DateField()

    def __str__(self):
        return str(self.user) + ' at "' + str(self.post) + '"'
