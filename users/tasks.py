from celery import shared_task
from django.core.mail import send_mail
from django.db.models import Count
from api.models import Post
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from users.models import CustomUser
from users.services.visit_db_service import VisitDataBaseService


@shared_task(name="send_top_post")
def send_top_post():
    most_liked_post = (
        Post.objects.annotate(num_likes=Count("like")).order_by("-num_likes").first()
    )
    if most_liked_post:
        context = {
            "post": most_liked_post,
        }

        users_emails = CustomUser.objects.values_list("email", flat=True)
        sender = "yamaltdinov.rustem2004@yandex.ru"
        html_content = render_to_string("email/most_liked_post_email.html", context)
        text_content = strip_tags(html_content)

        subject = f"Самый залайканный пост"
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=sender,
            to=list(users_emails),
        )
        email.attach_alternative(html_content, "text/html")
        email.send()


@shared_task(name="save_visits")
def save_visits():
    VisitDataBaseService().save_to_db()
