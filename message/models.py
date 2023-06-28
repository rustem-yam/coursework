from django.db import models
from users.models import CustomUser

# Create your models here.


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
        return str(self.sender) + " -> " + str(self.recipient) + ": " + str(self.text)
