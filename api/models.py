from django.db import models
from users.models import CustomUser


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateField()

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateField()

    def __str__(self):
        return self.text


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="received_messages"
    )
    text = models.TextField()
    send_date = models.DateField()

    def __str__(self):
        return self.text


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_added = models.DateField()

    def __str__(self):
        return self.post + "_" + self.user


class Friend(models.Model):
    user_1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_1_friends"
    )
    user_2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_2_friends"
    )
    date_added = models.DateField()

    def __str__(self):
        return self.user_1 + "_" + self.user_2
