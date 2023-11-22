import datetime
from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.contrib import admin
from simple_history.models import HistoricalRecords

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="received_messages"
    )
    text = models.TextField()
    send_date = models.DateTimeField()
    history = HistoricalRecords()

    @admin.display(
        boolean=True,
        ordering="send_date",
        description="Sent recently?",
    )
    def was_sent_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.send_date <= now

    def __str__(self):
        return (
            str(self.send_date)
            + " "
            + str(self.sender)
            + " -> "
            + str(self.recipient)
            + ": "
            + str(self.text)
        )
