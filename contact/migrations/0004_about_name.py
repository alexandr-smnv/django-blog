# Generated by Django 4.1.1 on 2022-10-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0003_about_social_imageabout"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="name",
            field=models.CharField(default="", max_length=50),
        ),
    ]
