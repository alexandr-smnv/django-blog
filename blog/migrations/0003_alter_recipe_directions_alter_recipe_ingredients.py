# Generated by Django 4.1.1 on 2022-10-20 18:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="directions",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients",
            field=ckeditor.fields.RichTextField(),
        ),
    ]