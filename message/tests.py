import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Message
from users.models import CustomUser


class MessageModelTests(TestCase):
    def test_was_sent_recently_with_future_message(self):
        """
        was_sent_recently() returns False for messages whose send_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_message = Message(send_date=time)
        self.assertIs(future_message.was_sent_recently(), False)

    def test_was_sent_recently_with_old_message(self):
        """
        was_sent_recently() returns False for messages whose send_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_message = Message(send_date=time)
        self.assertIs(old_message.was_sent_recently(), False)

    def test_was_sent_recently_with_recent_message(self):
        """
        was_sent_recently() returns True for messages whose send_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_message = Message(send_date=time)
        self.assertIs(recent_message.was_sent_recently(), True)


class ChatTests(TestCase):
    def test_no_messages(self):
        """
        If no messages exist, an appropriate message is displayed.
        """
        user_pk = 1
        response = self.client.get(reverse("message:chat", args=(user_pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no messages with  and  yet.")
        self.assertQuerySetEqual(response.context["messages"], [])
