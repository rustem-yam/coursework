# Generated by Django 4.2.2 on 2023-06-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(default="", max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="firstname",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="lastname",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="registration_date",
            field=models.DateField(default=""),
        ),
    ]
