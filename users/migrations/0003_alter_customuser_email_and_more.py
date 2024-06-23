# Generated by Django 4.2.2 on 2023-06-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_customuser_email_alter_customuser_firstname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                default="test@test.test", max_length=254, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="registration_date",
            field=models.DateField(default="2000-01-01"),
        ),
    ]
